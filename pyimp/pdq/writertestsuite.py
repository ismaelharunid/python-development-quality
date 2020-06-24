

from .common import *
from .simpletestsuite import SimpleTestSuite
from .testresults import TestResults


FORMATTER_KEYS = ("testsuite", "uid", "status", "code", "result", "expects"
    , "tags", "passed", "error", "extras", "tstamp")

PRINTTESTSUITE_FORMAT = " {:5d} {:27s} {:8s} [{:s}] \"{:s}\" expects={:s} result={:s} tags({:s})"
def PRINTTESTSUITE_FORMATTER(testsuite, uid, status, code, result, expects \
            , tags, passed, error, tstamp=0, duration=0, extras={}):
  ztstamp = TSTAMPS.str_tstamp(tstamp) if type(tstamp is float) else str(tstamp)
  zduration = TSTAMPS.str_since(duration) if type(duration is float) else repr(zduraction)
  ztags = ' '.join(tags) if isinstance(tags, Sequence) else repr(ztags)
  return PRINTTESTSUITE_FORMAT.format(uid, ztstamp, zduration, status, code \
      , repr(expects), repr(result), ztags)


class WriterTestSuite(SimpleTestSuite):
  
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

