
import sys, os, io, re, time, traceback
from functools import reduce
from collections import defaultdict
from collections.abc import Iterable, Sequence

UNIQUE_ID = 0

def unique_id():
  global UNIQUE_ID
  UNIQUE_ID += 1
  return UNIQUE_ID


seq_unique = lambda seq: type(seq)(reduce((lambda a,c: a if c in a else a+(c,)) \
    , seq, ()))
regex0 = re.compile(r'[^\w -]+', re.M)
regex1 = re.compile(r'[\s_-]+', re.M)
tag_clean = lambda tag: \
    regex1.sub('-', regex0.sub('', tag.strip('- \n').lower()))
tags_split = lambda tags, more=(): seq_unique(tuple(tag_clean(tag) for tag in \
    (tag.strip() for tag in tags.split(' ') if tag.strip())) + more)

def str_timestamp(epoch):
  tt = time.gmtime(epoch)
  return "{:s}:{:07.4f}+00".format(time.strftime("%Y-%M-%e:%H:%M", tt), epoch%60)

str_duration = lambda t: "{:8.4f}s".format(t)


StopExecution = type("StopExecutionType", (), {})()


class LRUStack(list):
  
  maxsize   = None
  
  def __init__(self, initializer=None, maxsize=100):
    self.maxsize = maxsize
    if initializer is None:
      super().__init__()
    else:
      super().__init__(initializer)
  
  def __trunc__(self):
    if self.maxsize is None:
      return
    while len(self) > self.maxsize:
      self.pop(0)
  
  def __imul__(self, value):
    super().__imul__(value)
    self.__trunc__()
  
  def __iadd__(self, key, values):
    super().__iadd__(value)
    self.__trunc__()
  
  def append(self, value):
    super().append(value)
    self.__trunc__()
  
  def insert(self, key, value):
    super().insert(key, value)
    self.__trunc__()
  
  def extend(self, iterable):
    super().extend(iterable)
    self.__trunc__()


class TestSuiteOperators(object):
  
  def issame(self, code, expects, scope={}, tags="issame"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result is expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def notsame(self, code, expects, scope={}, tags="notsame"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result is not expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def eq(self, code, expects, scope={}, tags="equals"):
    success, error = False, None
    #print("eq", code, expects, scope, tags)
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result == expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def ne(self, code, expects, scope={}, tags="not-equals"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result != expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def lt(self, code, expects, scope={}, tags="less-than"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result < expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def le(self, code, expects, scope={}, tags="less-than-equal"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result <= expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def gt(self, code, expects, scope={}, tags="greater-than"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result > expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def ge(self, code, expects, scope={}, tags="greater-than-equal"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result >= expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def contains(self, code, expects, scope={}, tags="contains"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = expects in result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def notcontains(self, code, expects, scope={}, tags="not-contains"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = expects not in result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def has(self, code, expects, scope={}, tags="has"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result in expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def nothas(self, code, expects, scope={}, tags="not-has"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = result not in expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def instance(self, code, expects, scope={}, tags="instanceof"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = isinstance(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def notinstance(self, code, expects, scope={}, tags="not-instanceof"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = not isinstance(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def subclass(self, code, expects, scope={}, tags="subclassof"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = issubclass(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def notsubclass(self, code, expects, scope={}, tags="not-subclassof"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = not issubclass(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  #TODO: Implement
  def catches(self, code, expects, scope={}, tags="catches"):
    pass
  
  #TODO: Implement
  def notcatches(self, code, expects, scope={}, tags="catches"):
    pass
  
  def throws(self, code, expects, scope={}, tags="throws"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
    except type(expects) as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      success = True
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def notthrows(self, code, expects, scope={}, tags="throws"):
    success, error = True, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
    except type(expects) as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      success = False
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def truish(self, code, expects=None, scope={}, tags="is-truish"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = bool(result)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)
  
  def nottruish(self, code, expects=None, scope={}, tags="not-truish"):
    success, error = False, None
    tstamp = self.now
    try:
      result = eval(code, self.scope, scope)
      success = not result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    duration = self.now - tstamp
    return self._test((success, error, result), code, expects, scope, tags, tstamp, duration)

TestSuiteOperators.equals = TestSuiteOperators.eq


class TestSuite(TestSuiteOperators):
  
  @staticmethod
  @property
  def Operators():
    return TestSuiteOperators
  
  _runs = None
  
  @property
  def runs(self):
    return self._runs
   
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
  def last_uid(self):
    return UNIQUE_ID
  
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
  
  def _test(self, ser, code, expects, scope, tags, tstamp=0, duration=0):
    success, error, result = ser
    if error and self.traceback:
      error = error.with_traceback(sys.exc_info()[2])
    item = \
        { "uid": self.get_uid()
        , "tags": tags_split(tags, self.tags)
        , "code": code
        , "result": result
        , "expects": expects
        , "passed": success
        , "error": error
        , "tstamp": tstamp
        , "duration": duration }
    self.runs.append( item )
    if success:
      self.passes += 1
    else:
      self.fails += 1
    if error:
      self.excepts += 1
    self.count += 1
    if StopExecution is self.report_item( **item ):
      sys.exit()
    return success

  def _report(self, uid=None, tags=None, code=None, result=None, expects=None \
      , passed=None, error=None):
    pass
  
  def __init__(self, name, tests=None, parent=None, scope={}, traceback=True
      , runsize=100):
    #print('init', name, tests, parent, scope, traceback, runsize)
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
    return unique_id()
  
  def query_runs(self, uid, *tags, **kwfilter):
    tags, run = set(tags), None
    try:
      return tuple(run for run in self.runs if (uid is None or uid == run['uid']) \
          and (not tags or tags.intersection(run['tags'])) \
          and all(k in run and run[k] == v for (k,v) in kwfilter.items()))
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
  
  def summary(self, also_children=True, indent=""):
    print("{:s}Summary for {:s}".format(indent, self.name))
    indent += "  "
    if len(self.children):
      passes, fails, errors, count = self.totals
      print("{:s}[PASS] this {:d}/{:d}, total {:d}/{:d}" \
          .format(indent, self.passes, self.count, passes, count))
      print("{:s}[FAIL] this {:d}/{:d}, total {:d}/{:d}" \
          .format(indent, self.fails, self.count, fails, count))
      print("{:s}[ERR]  this {:d}/{:d}, total {:d}/{:d}" \
          .format(indent, self.excepts, self.count, errors, count))
      print("{:s}with {:d} children".format(indent, len(self.children)))
    else:
      print("{:s}[PASS] {:d}/{:d}".format(indent, self.passes, self.count))
      print("{:s}[FAIL] {:d}/{:d}".format(indent, self.fails, self.count))
      print("{:s}[ERR]  {:d}/{:d}".format(indent, self.excepts, self.count))
      print("{:s}no children".format(indent))
    indent += "  "
    for child in self.children:
      child.summary(also_children, indent)


FORMATTER_KEYS = ("testsuite", "uid", "status", "code", "result", "expects"
    , "tags", "passed", "error", "extras", "tstamp")

PRINTTESTSUITE_FORMAT = " {:5d} {:27s} {:8s} [{:s}] \"{:s}\" expects={:s} result={:s} tags({:s})"
def PRINTTESTSUITE_FORMATTER(testsuite, uid, status, code, result, expects \
            , tags, passed, error, tstamp=0, duration=0, extras={}):
  ztstamp = str_timestamp(tstamp) if type(tstamp is float) else repr(tstamp)
  zduration = str_duration(duration) if type(duration is float) else repr(zduraction)
  ztags = ' '.join(tags) if isinstance(tags, Sequence) else repr(ztags)
  return PRINTTESTSUITE_FORMAT.format(uid, ztstamp, zduration, status, code \
      , repr(expects), repr(result), ztags)


class WriterTestSuite(TestSuite):
  
  wroter = None
  formatter = None
  verbosity = 1
  
  def __init__(self, name, tests=None, parent=None, scope={}, traceback=True
      , runsize=100, writer=print, formatter=PRINTTESTSUITE_FORMATTER
      , verbosity=2):
    self.writer = writer
    self.formatter = formatter
    self.verbosity = verbosity
    super().__init__(name, tests, parent, scope, traceback, runsize)
  
  def report(self, also_children=True, **kwfilters):
    print("go through all runs and print them,then their children if also_children")
    pass
  
  def report_item(self, uid, tags='', code='', result=None, expects=None \
      , passed=0, error=0, tstamp=0, duration=0, extras={}):
    line = self._report(uid, tags, code, result, expects, passed, error
        , tstamp, duration, extras)
    if line is not None and callable(self.writer):
      self.writer(line)
  
  def _report(self, uid, tags='', code='', result=None, expects=None \
      , passed=0, error=0, tstamp=0, duration=0, extras={}):
    if self.verbosity >= 4 or (self.verbosity >= 3 and error) \
        or (self.verbosity >= 2 and not passed) \
        or (self.verbosity >= 1 and not passed and error):
      status = 'PASS' if passed else 'ERROR' if error else 'FAIL'
      if callable(self.formatter):
        return self.formatter(self, uid, status, code, result, expects \
            , tags, passed, error, tstamp, duration, extras)
      elif type(self.formatter) is str:
        return self.formatter.format_map(dict(kv for kv in zip(FORMATTER_KEYS \
            , (self, uid, status, code, result, expects, tags, passed \
            , error, tstamp, duration, extras))))
      elif self.formatter is True:
        return (self, uid, status, code, result, expects, tags, passed \
            , error, tstamp, duration, extras)
      elif self.formatter is not None:
        raise TypeError("invalid formatter, expected a callable or format_map" \
            " string but found {:s}".format(repr(self.formatter)))

