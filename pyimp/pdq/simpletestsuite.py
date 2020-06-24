

from .common import *
from .testsuite import TestSuite
from .testops import TestSuiteOperators
from .testresults import TestResults
from .events import EventListener


class SimpleTestSuite(TestSuite, TestSuiteOperators, EventListener):
  
  def __init__(self, *args, **kwargs):
    EventListener.__init__(self, ("run,pass,fail,exception"))
    super().__init__(*args, **kwargs)
    
  def do_triggers(self, runitem, *args, **kwargs):
    pass
  
