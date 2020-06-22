
import sys, os, io, re, traceback
from functools import reduce


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
  
  def lt(self, code, expects, scope={}, tags="greater-than"):
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
      success = result in expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def notcontains(self, code, expects, scope={}, tags="not-contains"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = result not in expects
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def has(self, code, expects, scope={}, tags="has"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = expects in result
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def nothas(self, code, expects, scope={}, tags="not-has"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = expects not in result
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
      success = subclass(result, expects)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def notsubclass(self, code, expects, scope={}, tags="not-subclassof"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = not subclass(result, expects)
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
  
  def true(self, code, expects=None, scope={}, tags="is-true"):
    success, error = False, None
    try:
      result = eval(code, self.scope, scope)
      success = bool(result)
    except Exception as e:
      #print(e)
      #traceback.print_exc(file=sys.stdout)
      result = error = e
    return self._test((success, error, result), code, expects, scope, tags)
  
  def false(self, code, expects=None, scope={}, tags="is-false"):
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
  
  name = None
  tests = None
  scope = None
  parent = None
  traceback = None
  children = None
  runs = None
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
    elif error:
      self.excepts += 1
    else:
      self.fails += 1
    self.count += 1
    if StopExecution is self._report( **item ):
      sys.exit()
    return success

  def _report(self, uid=None, tags=None, code=None, result=None, expects=None \
      , passed=None, error=None):
    pass
  
  def __init__(self, name, *tests, scope=None, parent=None, traceback=None):
    self.name = tag_clean(name)
    self.tags = seq_unique(parent.tags+(self.name,)) if parent else (self.name,)
    self.tests = list(tests)
    self.scope = scope
    self.parent = parent
    self.traceback = traceback
    self.children = []
    self.runs = []
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
    tags = set(tags)
    return tuple(run for run in self.runs if (uid is None or uid == run['uid']) \
        and (not tags or tags.intersection(run['tags'])) \
        and all(k in run and run[k] == v for (k,v) in kwfilter.items))
  
  def get_last_run(self):
    last_run = self.query_runs(self.last_uid)
    return last_run and last_run[0] or None
  
  def register(self, child):
    if child not in self.children:
      self.children.append( child )
  
  def add_test(self, methodname, args, kwargs={}):
    if hasattr(TestSuiteOperators, methodname):
      raise ValueError("Unsupported methodname {:s}".format(repr(methodname)))
    self.tests.append( (methodname, args, kwargs) )
    return self
  
  def add_many_test(self, tests):
    self.tests.extend(tests)
    return self
  
  def run_tests(self):
    for child in self.children:
      child.run_tests()
    for (methodname, args, kwargs) in self.tests:
      getattr(self, methodname)(self, *args, **kwargs)
    return self


class PrintTestSuite(TestSuite):
  
  verbosity = 1
  
  def __init__(self, name, *tests, scope=None, parent=None, traceback=None
      , verbosity=2):
    self.verbosity = verbosity
    super().__init__(name, *tests, scope, parent, traceback)
  
  def _report(self, uid=None, tags=None, code=None, result=None, expects=None \
      , passed=None, error=None):
    if self.verbosity >= 4 or (self.verbosity >= 3 and error) \
        or (self.verbosity >= 2 and not passed) \
        or (self.verbosity >= 1 and not passed and error):
      print(uid, tags, code, result, expects, passed, error)

