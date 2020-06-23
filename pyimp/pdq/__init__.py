
from .testsuite import TestSuite, WriterTestSuite \
    , TestSuiteOperators, StopExecution


try:
  execfile = lambda fpath: exec(open(fpath).read())
except:
  pass

