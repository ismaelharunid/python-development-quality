

from .common import *
from datetime import datetime, timedelta, timezone


DT_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
TMARK_FORMAT = "{:.6f}"


dt_now = lambda: \
    datetime.now(tzinfo=timezone.utc, microsecond=100)

now = lambda: \
    (dt_now() - DT_EPOCH) / timedelta(seconds=1)


class TimeStamps(object):
  
  _marks = None
  _tmark_format = None
  
  @property
  def dt_now(self):
    return datetime.now(timezone.utc)
  
  @property
  def now(self):
    return (self.dt_now - DT_EPOCH) / timedelta(seconds=1)
  
  def __init__(self, tmark_format=TMARK_FORMAT):
    self._marks = {}
    self._tmark_format = tmark_format
    self.mark(None)
  
  def __timedate__(self, dtstamp):
    if isinstance(dtstamp, float):
      return datetime.fromtimestamp(dtstamp, tz=timezone.utc)
    elif isdtseq(dtstamp):
      return datetime(dtstamp, tzinfo=timezone.utc)
    elif dtstamp is None:
      return self.dt_now
    elif not isinstance(dtstamp, datetime):
      raise ValueError("Invalid dtstamp, expected a timestamp(float), datetime" \
          " or None but found {:s}".format(repr(dtstamp)))
  
  def __float__(self, dtstamp=None):
    if isinstance(dtstamp, float):
      return dtstamp
    dtstamp = self.__datetime__(dtstamp)
    return (dtstamp - DT_EPOCH) / timedelta(seconds=1)
  
  def __str__(self):
    return self.str_since_mark(None, False)
  
  def __repr__(self):
    return '{:s}("{:s}")'.format(self.__class__.__name__, str(self))
  
  def str_tduration(self, tduration):
    return self._tmark_format.format(tduration)
  
  def since(self, dtstamp=None):
    return self.now - self.__float__(dtstamp)
  
  def str_since(self, dtstamp=None):
    tmark = self.since(dtstamp)
    return self._tmark_format.format(tmark)
  
  def mark(self, key=None):
    old_mark = self._marks[key] if key in self._marks else None
    self._marks[key] = self.now
    return old_mark
  
  def since_mark(self, key=None, pop=True):
    mark = self._marks.pop(key) if pop else self._marks[key]
    return self.now - mark
  
  def str_since_mark(self, key=None, pop=True):
    tmark = self.since_mark(key, pop)
    return self._tmark_format.format(tmark)
  
  def clear_marks(self):
    #while self._marks:
    #  self._makes.popitem()
    self._marks = {}
  
  def str_tstamp(self, dtstamp=None):
    return self.tstamp(dtstamp).isoformat()

# alias for Timestamp
TimeStamps.tstamp = TimeStamps.__float__
TimeStamps.tmark = TimeStamps.since_mark
TimeStamps.str_tmark = TimeStamps.str_since_mark

