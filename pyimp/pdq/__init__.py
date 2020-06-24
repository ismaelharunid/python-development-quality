
from .common import *
from .testresults import TestResults
from .testsuite import TestSuite
from .simpletestsuite import SimpleTestSuite
from .writertestsuite import WriterTestSuite
from .events import EventListener, Event, StopPropagation


try:
  execfile = lambda fpath: exec(open(fpath).read())
except:
  pass

