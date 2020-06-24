
from collections.abc import Iterable, Mapping, Sequence
from .uniqueids import unique_id_generator
UID = unique_id_generator()

from .timestamps import TimeStamps
TSTAMPS = TimeStamps()

from .tagutil import tag_clean, tags_split, tags_join

StopExecution = type("StopExecutionType", (), {})()

isntuple = lambda s,n:  isinstance(s, tuple) and n == len(s)
isnseq = lambda s,n:  isinstance(s, Sequence) and n == len(s)
isdtseq = lambda s: isinstance(s, Sequence) and 3 <= len(s) and len(s) <= 7

from sys import stdin, stdout, stderr
from os import linesep as os_linesep
def write(ostream, *tokens):
  for token in tokens:
    s = str(token)
    if len(s) != ostream.write(s):
      pass

def writeln(ostream, *tokens):
  write(ostream, *tokens)
  write(ostream, os_linesep)
