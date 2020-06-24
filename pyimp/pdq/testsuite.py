
import sys, os, io, time, traceback
from functools import reduce
from collections import defaultdict

from .common import *
from .lrustacks import LRUStack


class TestSuite(object):
  
  @staticmethod
  @property
  def Operators():
    return TestSuiteOperators
  
  _runs = None
  
  @property
  def runs(self):
    return self._runs
   
  last_uid = None
  name = None
  tests = None
  scope = None
  parent = None
  traceback = None
  children = None
  passes = None
  failures = None
  excepts = None
  test = None
  
  @property
  def now(self):
    return time.time()
  
  @property
  def totals(self):
    passed = self.passes or 0
    failed = self.failures or 0
    errors = self.excepts or 0
    count = self.count or 0
    if self.children:
      for child in self.children:
        ttls = child.totals
        passed += ttls[0] or 0
        failed += ttls[1] or 0
        errors += ttls[2] or 0
        count  += ttls[3] or 0
    return ( passed, failed, errors, count )
  
  def ontest(self, test):
    if test.exception and self.traceback:
      test.exception = test.exception.with_traceback(sys.exc_info()[2])
    test.tags = tags_split(test.tags, self.tags)
    self.runs.append( test )
    if test.passed:
      self.passes += 1
    else:
      self.fails += 1
    if test.exception:
      self.excepts += 1
    self.count += 1
    self.do_triggers( test )
    return test.passed
  
  def do_triggers(self, runitem, *args, **kwargs):
    pass
  
  def __init__(self, name, tests=None, parent=None, scope={}, traceback=True
      , runsize=100):
    #print('init', name, tests, parent, scope, traceback, runsize)
    self.last_uid = None
    self.name = tag_clean(name)
    self.tags = (self.name,)
    self.tests = list(tests) if tests else []
    self.scope = scope if scope else {}
    self.parent = parent or None
    self.traceback = traceback
    self.children = []
    self._runs = LRUStack(maxsize=runsize)
    self.passes = 0
    self.fails = 0
    self.excepts = 0
    self.count = 0
    if parent:
      parent.register(self)
  
  def get_uid(self):
    self.last_uid = UID.__next__()
    return self.last_uid
  
  def query_runs(self, uid, *tags, **kwfilter):
    tags, run = set(tags), None
    try:
      return tuple(run for run in self.runs if (uid is None or uid == run.uid) \
          and (not tags or tags.intersection(run.tags)) \
          and all(hasattr(run, k) and getattr(run, k) == v for (k,v) in kwfilter.items()))
    except Exception as e:
      #print(uid, tags, kwfilter, run)
      raise e
  
  def get_last_run(self):
    last_run = self.query_runs(self.last_uid)
    return last_run and last_run[0] or None
  
  def unregister(self, child):
    if child in self.children:
      self.children.remove(child)
  
  def register(self, child):
    if child not in self.children:
      self.children.append( child )
      tags = list(self.tags)
      for tag in child.tags:
        if tag not in tags:
          tags.append(tag)
      self.tags = tuple(tags)
  
  def add(self, methodname, code, *args, **kwargs):
    if hasattr(self.__class__.Operators, methodname):
      raise ValueError("Unsupported methodname {:s}".format(repr(methodname)))
    #print('before append', self.tests)
    item = (methodname, code, args, kwargs)
    #print('item', item)
    self.tests.append( item )
    #print('after append', self.tests)
    return self
  
  def add_many(self, tests):
    self.tests.extend(tests)
    return self
  
  def flush(self, print_summary=True):
    self.run_tests()
    self.summary()
    self.clear_runs()
  
  def teardown(self, also_children=True):
    if also_children:
      for child in self.children:
        child.teardown(also_children)
        self.unregister(child)
    self.clear_runs()
    self.tests = None
    self.scope = None
    self.parent = None
    self.children = None
    self.passes = 0
    self.fails = 0
    self.excepts = 0
    self.count = 0
  
  def clear_runs(self, also_children=True):
    if also_children:
      for child in self.children:
        child.clear_runs()
    self._runs = []
  
  def run_tests(self):
    for child in self.children:
      child.run_tests()
    for (methodname, code, args, kwargs) in self.tests:
      #print("run_tests", args, kwargs)
      getattr(self, methodname)(code, *args, **kwargs)
    return self
  
  def summary(self, also_children=True, out=sys.stdout, indent=""):
    writeln(out, "{:s}Summary for {:s}".format(indent, self.name))
    indent += "  "
    if len(self.children):
      passes, fails, errors, count = self.totals
      writeln(out, "{:s}[PASS] this {:d}/{:d}, total {:d}/{:d}" \
          .format(indent, self.passes, self.count, passes, count))
      writeln(out, "{:s}[FAIL] this {:d}/{:d}, total {:d}/{:d}" \
          .format(indent, self.fails, self.count, fails, count))
      writeln(out, "{:s}[ERR]  this {:d}/{:d}, total {:d}/{:d}" \
          .format(indent, self.excepts, self.count, errors, count))
      writeln(out, "{:s}with {:d} children".format(indent, len(self.children)))
    else:
      writeln(out, "{:s}[PASS] {:d}/{:d}".format(indent, self.passes, self.count))
      writeln(out, "{:s}[FAIL] {:d}/{:d}".format(indent, self.fails, self.count))
      writeln(out, "{:s}[ERR]  {:d}/{:d}".format(indent, self.excepts, self.count))
      writeln(out, "{:s}no children".format(indent))
    indent += "  "
    for child in self.children:
      child.summary(also_children, out, indent)
  

