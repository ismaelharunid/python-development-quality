

from .common import *
from .testsuite import TestSuite
from .testresults import TestResults

"""
assertEqual(a, b)	a == b	 
assertNotEqual(a, b)	a != b	 
assertTrue(x)	bool(x) is True	 
assertFalse(x)	bool(x) is False	 
assertIs(a, b)	a is b	3.1
assertIsNot(a, b)	a is not b	3.1
assertIsNone(x)	x is None	3.1
assertIsNotNone(x)	x is not None	3.1
assertIn(a, b)	a in b	3.1
assertNotIn(a, b)	a not in b	3.1
assertIsInstance(a, b)	isinstance(a, b)	3.2
assertNotIsInstance(a, b)	not isinstance(a, b)	3.2
"""

class TestSuiteOperators(object):
  
  def istruish(self, code, tags="istruish", scope={}):
    test_results = TestResults(self, code, (), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = bool(result)
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def nottruish(self, code, tags="nottruish", scope={}):
    test_results = TestResults(self, code, (), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = not result
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def issame(self, code, expects, tags="issame", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result is expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notsame(self, code, expects, tags="notsame", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result is not expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def isequal(self, code, expects, tags="isequal", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result == expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notequal(self, code, expects, tags="notequal", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result != expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def isless(self, code, expects, tags="isless", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result < expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notless(self, code, expects, tags="notless", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result >= expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def ismore(self, code, expects, tags="isless", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result > expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notmore(self, code, expects, tags="notless", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result <= expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def isntuple(self, code, expects, tags="isntuple", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = type(result) is tuple and len(result) == int(expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notntuple(self, code, expects, tags="notntuple", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = type(result) is not tuple or len(result) != int(expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result not in expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def isnsequence(self, code, expects, tags="isnsequence", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = isinstance(result, Sequence) and len(result) == int(expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notnsequence(self, code, expects, tags="notnsequence", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = not isinstance(result, Sequence) or len(result) != int(expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result not in expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def isin(self, code, expects, tags="isin", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result in expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notin(self, code, expects, tags="notin", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = result not in expects
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def iscontaining(self, code, expects, tags="iscontaining", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = expects in result
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notcontaining(self, code, expects, tags="notcontaining", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    passed = expects not in result
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def istype(self, code, expects, tags="istype", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = type(result) is expects
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def nottype(self, code, expects, tags="nottype", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = type(result) is not expects
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def isinstance(self, code, expects, tags="isinstance", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = isinstance(result, expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notinstance(self, code, expects, tags="notinstance", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = not isinstance(result, expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def issubclass(self, code, expects, tags="issubclass", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = issubclass(result, expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notsubclass(self, code, expects, tags="notsubclass", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      result = eval(code, self.scope, scope)
      passed = not issubclass(result, expects)
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  #TODO: Implement, check if exceotion happened but we didn't get it
  def iscatching(self, code, expects, tags="iscatching", scope={}):
    raise NotImplementedError('iscatching')
  
  #TODO: Implement, check if exceotion happened but we caught it
  def notcatching(self, code, expects, tags="notcatching", scope={}):
    raise NotImplementedError('notcatching')
  
  def isthrowing(self, code, expects, tags="isthrowing", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      try:
        eval(code, self.scope, scope)
        result, passed = None, False
      except expects as expected:
        result, passed = expected, True
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception
  
  def notthrowing(self, code, expects, tags="notthrowing", scope={}):
    test_results = TestResults(self, code, (expects,), tags, scope)
    try:
      try:
        eval(code, self.scope, scope)
        result, passed = None, True
      except expects as expected:
        result, passed = expected, False
    except Exception as exc:
      return test_results.finalize( False, None, exc ) # failed, no-result, exception
    return test_results.finalize( passed, result ) # failed, no-result, exception

TestSuiteOperators.iseq = TestSuiteOperators.isequal
TestSuiteOperators.isne = TestSuiteOperators.notequal
TestSuiteOperators.islt = TestSuiteOperators.isless
TestSuiteOperators.isge = TestSuiteOperators.notless
TestSuiteOperators.isgt = TestSuiteOperators.ismore
TestSuiteOperators.isle = TestSuiteOperators.notmore


