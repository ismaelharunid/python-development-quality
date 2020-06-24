

from .common import *


class TestResults(object):
  
  testsuite = None
  uid       = None
  code      = None
  args      = None
  tags      = None
  scope     = None
  tstamp    = None
  tduration = None
  passed    = None
  result    = None
  exception = None
  
  def __init__(self, testsuite, code, args, tags="", scope=None, tstamp=None
      , uid=None):
    self.tduration = self.passed = self.result = self.exception = None
    self.testsuite = testsuite
    self.code = code
    self.args = args
    self.tags = tags
    self.scope = scope
    self.tstamp = tstamp or TSTAMPS.now
    self.uid = uid or testsuite.get_uid()
  
  def __repr__(self):
    return self.__str__()
  
  def __str__(self):
    return "{:s}({:s})".format( self.__class__.__name__, ' '.join( 
        ( "testsuite.name="+repr(self.testsuite.name)
        , "uid="+repr(self.uid)
        , "code="+repr(self.code)
        , "args="+repr(self.args)
        , "tags="+repr(self.tags)
        , "scope={...}"
        , "tstamp="+repr(self.tstamp)
        , "tduration="+repr(self.tduration)
        , "passed="+repr(self.passed)
        , "result="+repr(self.result)
        , "exception="+repr(self.exception) )) )
  
  def finalize(self, passed, result, exception=None):
    self.tduration = TSTAMPS.now - self.tstamp
    self.passed = passed
    self.result = result
    self.exception = exception
    if self.testsuite:
      self.testsuite.ontest(self)
    return passed



