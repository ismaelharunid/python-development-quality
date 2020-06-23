
import sys, os, io, re, traceback
from functools import reduce
from collections import defaultdict


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


class StopExecutionType:
  pass

StopExecution = StopExecutionType()


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
    try:
      result = eval(code, self.scope, scope)
      success = result is expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def notsame(self, code, expects, scope={}, tags="notsame"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result is not expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def eq(self, code, expects, scope={}, tags="equals"):
    success, error = False, None
    #print("eq", code, expects, scope, tags)
    try:
      result = eval(code, self.scope, scope)
      success = result == expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def ne(self, code, expects, scope={}, tags="not-equals"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result != expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def lt(self, code, expects, scope={}, tags="less-than"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result < expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def le(self, code, expects, scope={}, tags="less-than-equal"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result <= expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def gt(self, code, expects, scope={}, tags="greater-than"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result > expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def ge(self, code, expects, scope={}, tags="greater-than-equal"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result >= expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def contains(self, code, expects, scope={}, tags="contains"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = expects in result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def notcontains(self, code, expects, scope={}, tags="not-contains"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = expects not in result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def has(self, code, expects, scope={}, tags="has"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result in expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def nothas(self, code, expects, scope={}, tags="not-has"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result not in expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def instance(self, code, expects, scope={}, tags="instanceof"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = isinstance(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def notinstance(self, code, expects, scope={}, tags="not-instanceof"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = not isinstance(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def subclass(self, code, expects, scope={}, tags="subclassof"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = issubclass(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def notsubclass(self, code, expects, scope={}, tags="not-subclassof"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = not issubclass(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def catch(self, code, expects, scope={}, tags="catches"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
    except type(expects) as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      success = True
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def truish(self, code, expects=None, scope={}, tags="is-truish"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = bool(result)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def nottruish(self, code, expects=None, scope={}, tags="not-truish"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = not result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)

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
  exceptions = None
  test = None
  
  @property
  def last_uid(self):
    return UNIQUE_ID
  
  def _test(self, ser, code, expects, scope, tags):
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
        , "error": error }
    self.runs.append( item )
    if success:
      self.passes += 1
    else:
      self.fails += 1
    if error:
      self.excepts += 1
    self.count += 1
    if StopExecution is self._report( **item ):
      sys.exit()
    return success

  def _report(self, uid=None, tags=None, code=None, result=None, expects=None \
      , passed=None, error=None):
    pass
  
  def __init__(self, name, tests=None, parent=None, scope={}, traceback=True
      , runsize=100):
    #print('init', name, tests, parent, scope, traceback, runsize)
    self.name = tag_clean(name)
    self.tags = seq_unique(parent.tags+(self.name,)) if parent else (self.name,)
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
  
  def clear_runs(self, also_children=True):
    if also_children:
      for child in self.children:
        child.clear_runs()
    self.runs = []
  
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
  
  def register(self, child):
    if child not in self.children:
      self.children.append( child )
  
  def add_test(self, methodname, args, kwargs={}):
    if hasattr(self.__class__.Operators, methodname):
      raise ValueError("Unsupported methodname {:s}".format(repr(methodname)))
    #print('before append', self.tests)
    item = (methodname, args, kwargs)
    #print('item', item)
    self.tests.append( item )
    #print('after append', self.tests)
    return self
  
  def add_many_test(self, tests):
    self.tests.extend(tests)
    return self
  
  def run_tests(self):
    for child in self.children:
      child.run_tests()
    for (methodname, args, kwargs) in self.tests:
      #print("run_tests", args, kwargs)
      getattr(self, methodname)(*args, **kwargs)
    return self
  
  def summary(self, also_children=True, indent=""):
    print("{:s}Summary for {:s}".format(indent, self.name))
    indent += "  "
    print("{:s}[PASS] {:d}/{:d}".format(indent, self.passes, self.count))
    print("{:s}[FAIL] {:d}/{:d}".format(indent, self.fails, self.count))
    print("{:s}[ERR]  {:d}/{:d}".format(indent, self.excepts, self.count))
    if len(self.children):
      print("{:s}with {:d} children".format(indent, len(self.children)))
    else:
      print("{:s}with no children".format(indent))
    indent += "  "
    for child in self.children:
      child.summary(also_children, indent)


FORMATTER_KEYS = ("testsuite", "uid", "status", "code", "result", "expects"
    , "tags", "passed", "error", "extras", "tstamp")

PRINTTESTSUITE_FORMAT = "{:10s} {:3d} {:s} {:-40s} result={:s} expects={:s} tags({:s})"
def PRINTTESTSUITE_FORMATTER(testsuite, uid, status, code, result, expects \
            , tags, passed, error, tstamp=None, extras={}):
  tstamp = time.str(tstamp) if type(tstamp) in (float, time.time) else \
      repr(t_stamp)
  return PRINTTESTSUITE_FORMAT.format(tstamp, uid, status, code, result, expects, tags)


class WriterTestSuite(TestSuite):
  
  formatter = None
  verbosity = 1
  
  def __init__(self, name, tests=None, parent=None, scope={}, traceback=True
      , runsize=100, writer=print, formatter=PRINTTESTSUITE_FORMATTER
      , verbosity=2):
    self.formatter = formatter
    self.verbosity = verbosity
    super().__init__(name, tests, parent, scope, traceback, runsize)
  
  def report(self, also_children=True, **kwfilters):
    print("go through all runs and print them,then their children if also_children")
    pass
  
  def report_item(self, uid, tags='', code='', result=None, expects=None \
      , passed=0, error=0, tstamp=0, extras={}):
    line = self._report(self, uid, tags, code, result, expects, passed, error
        , tstamp, extras)
    if callable(self._writer):
      self._writer(line)
  
  def _report(self, uid, tags='', code='', result=None, expects=None \
      , passed=0, error=0, tstamp=0, extras={}):
    if self.verbosity >= 4 or (self.verbosity >= 3 and error) \
        or (self.verbosity >= 2 and not passed) \
        or (self.verbosity >= 1 and not passed and error):
      status = 'PASS' if passed else 'ERROR' if error else 'FAIL' 
      if callable(self.formatter):
        return self.formatter(self, uid, status, code, result, expects \
            , tags, passed, error, tstamp, extras)
      elif type(self.formatter) is str:
        return self.formatter.format_map(dict(kv for kv in zip(FORMATTER_KEYS \
            , (self, uid, status, code, result, expects, tags, passed \
            , error, tstamp, extras))))
      elif self.formatter is True:
        return (self, uid, status, code, result, expects, tags, passed \
            , error, tstamp, extras)
      elif self.formatter is not None:
        raise TypeError("invalid formatter, expected a callable or format_map" \
            " string but found {:s}".format(repr(self.formatter)))

