

from .common import *
from .simpletestsuite import SimpleTestSuite
from .testresults import TestResults


FORMATTER_KEYS = ("testsuite", "uid", "status", "code", "result", "expects"
    , "tags", "passed", "exception", "extras", "tstamp")

LINE_FORMAT = " {uid:5s} {tstamp:27s} {tduration:8s} [{status:s}] \"{code:s}\" args={args:s} result={result:s} tags({tags:s})"
EXTENDED_LINE_FORMAT = "+      {:s}"
def LINE_FORMATTER(mapping):
  lm = dict(mapping)
  tstamp = TSTAMPS.str_tstamp(lm.pop("tstamp")) \
      if type(lm["tstamp"] is float) else \
      str(lm.pop("tstamp"))
  tduration = "{:9.6f}".format(lm.pop("tduration")) \
      if type(lm["tduration"] is float) else \
      repr(lm.pop("tduration"))
  tags = ' '.join(lm.pop("tags")) if isinstance(lm["tags"], Sequence) else \
      repr(lm.pop("tags"))
  for k in lm.keys():
    lm[k] = str(lm[k])
  lm['tstamp'] = tstamp
  lm['tduration'] = tduration
  lm['tags'] = tags
  #print(LINE_FORMAT)
  #print(lm)
  line = LINE_FORMAT.format(**lm)
  if "extras" in mapping:
    extras = mapping["extras"]
    lines = [ line ]
    if isinstance(extras, Sequence):
      lines += list(EXTENDED_LINE_FORMAT.format(str(x)) for x in extras)
    elif isinstance(extras, Mapping):
      lines += list(EXTENDED_LINE_FORMAT \
          .format("{:s)=(:s)".format(repr(k), repr(x)) \
          for (k,x) in extras.items()))
    line = '\n'.join(lines)
  return line


class WriterTestSuite(SimpleTestSuite):
  
  wroter = None
  formatter = None
  verbosity = 1
  
  def __init__(self, name, tests=None, parent=None, scope={}, traceback=True
      , runsize=100, writer=print, formatter=LINE_FORMATTER
      , verbosity=2):
    self.writer = writer
    self.formatter = formatter
    self.verbosity = verbosity
    super().__init__(name, tests, parent, scope, traceback, runsize)
  
  def report(self, also_children=True, **kwfilters):
    if callable(self.writer):
      for run in self._runs:
        self.report_item(run, **kwfilters)
      if also_children:
        for child in self.children:
          child.report(also_children, **kwfilters)
  
  def report_item(self, run, **kwfilters):
    if (self.verbosity >= 4 or (self.verbosity >= 3 and run.exception) \
        or (self.verbosity >= 2 and not run.passed) \
        or (self.verbosity >= 1 and not run.passed and run.exception)) \
        and callable(self.writer):
      line = self._report(run)
      if line is not None:
        self.writer(line)
  
  def _report(self, run, **kwfilters):
    mapping = vars(run)
    mapping["status"] = 'PASS' if run.passed else \
        'ERROR' if run.exception else \
        'FAIL'
    #print(mapping)
    if callable(self.formatter):
      return self.formatter(mapping)
    elif type(self.formatter) is str:
      return self.formatter.format(mapping)
    elif self.formatter is True:
      return mapping
    elif self.formatter is not None:
      raise TypeError("invalid formatter, expected a callable or format_map" \
          " string but found {:s}".format(repr(self.formatter)))

