
from .testsuite import TestSuite, PrintTestSuite \
    , TestSuiteOperators, StopExecution


try:
  execfile = lambda fpath: exec(open(fpath).read())
except:
  pass

