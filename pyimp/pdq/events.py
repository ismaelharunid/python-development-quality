

from .common import *


StopPropagation = type("StopPropagationType", (), {})()


class Event(object):
  
  type      = None
  callbacks = None
  occurs    = None
  options   = None
  extras    = None
  kwextras  = None
  
  def __init__(self, eventtype, callbacks, options={}, occurs=None
      , *extras, **kwextras):
    if type(eventtype) is not str:
      raise ValueError("eventtype expects a str, but found: {:s}" \
          .format(repr(eventtype)))
    if callable(callbacks):
      callbacks = (callbacks,)
    if any(not callable(cb) for cb in callbacks):
      raise ValueError("callbacks excepts a callable or sequence of them" \
          ", but found: {:s}".format(repr(callbacks)))
    if options and not isinstance(options, Mapping):
      raise ValueError("options expects a Mapping or None, but found: {:s}" \
          .format(repr(options)))
    if occurs and type(options) != int:
      raise ValueError("occurs expects an int or None, but found: {:s}" \
          .format(repr(occurs)))
    self.type = eventtype
    self.callbacks = callbacks
    self.options = options or {}
    self.occurs = occurs or None
    self.extras = extras
    self.kwextras = kwextras
  
  def istriggered(self, *args, **kwargs):
    return True


class EventListener(object):
  
  _parent         = None
  _events         = None
  _indextypes     = None
  _indexes        = None
  
  def __init__(self, types=None, parent=None):
    if not types:
      types = []
    elif type(types) is str:
      types = list(key for key in (key.strip() \
          for key in types.split(',')) if key)
    elif isinstance(types, Sequence) \
        and all(type(name) is str for name in types):
      types = list(types)
    else:
      raise ValueError("types expects a commas sperator str, " \
          "sequence of eventtypes or None but found {:s}" \
          .format(repr(name)))
    indextypes = []
    self._parent = parent or self
    self._events = []
    self.indexes = {}
    self.indexes['type'] = []
    indextypes.append( 'type' )
    if 'type' in types:
      types.remove('type')
    for name in types:
      if name in indextypes:
        continue
      indextypes.append( name )
      self.indexes[name] = []
      types.remove(name)
    self._indextypes = tuple(indextypes)
  
  def add(self, event):
    if not isinstance(event, Event):
      raise ValueError("event expects an Event instance but found {:s}" \
          .format(repr(event)))
    print(event)
    eventtype = event.type
    if eventtype not in self._indextypes:
      raise ValueError("unsupported eventtype {:s}" \
          .format(repr(eventtype)))
    self._indexes[eventtype].append(event)
    self._indexes['callbacks'].append(event)
    self._events.append(event)
  
  def remove(self, types=None, events=None, callbacks=None):
    if types:
      if not isinstance(types, Sequence):
        types = (types,)
      for eventtype in types:
        if type(eventtype) is not str or eventtype not in self._indextypes:
          raise ValueError("types expects supported event types as a str" \
              " but found {:s}".format(repr(eventtype)))
        evs = self._indextypes[eventtype]
        while event in evs:
          evs.remove(event)
          while event in self.events:
            self._events.remove(event)
    if events:
      if not isinstance(events, Sequence):
        events = (events,)
      for event in events:
        if not isinstance(event, Event):
          raise ValueError("event expects an Event instance but found {:s}" \
              .format(repr(event)))
        for evs in self._indexes.values():
          while event in evs:
            evs.remove(event)
        while event in self.events:
          self._events.remove(event)
    if callbacks:
      if not callable(callbacks):
        callbacks = (callbacks,)
      for cb in callbacks:
        if not callable(cb):
          raise ValueError("callbacks expects callables" \
              " but found {:s}".format(repr(callbacks)))
        evs = self._indextypes['callbacks']
        while event in evs:
          evs.remove(event)
          while event in self.events:
            self._events.remove(event)
  
  def trigger(self, types=None, events=None, callbacks=None, *args, **kwargs):
    accum = []
    if types:
      if not isinstance(types, Sequence):
        types = (types,)
      for eventtype in types:
        if type(eventtype) is not str or eventtype not in self._indextypes:
          raise ValueError("types expects supported event types as a str" \
              " but found {:s}".format(repr(eventtype)))
        evs = self._indextypes[eventtype]
        while event in evs:
          if event not in accum:
            accum.append(event)
    if events:
      if not isinstance(events, Sequence):
        events = (events,)
      for event in events:
        if not isinstance(event, Event):
          raise ValueError("event expects an Event instance but found {:s}" \
              .format(repr(event)))
        for evs in self._indexes.values():
          while event in evs:
            if event not in accum:
              accum.append(event)
    if callbacks:
      if not callable(callbacks):
        callbacks = (callbacks,)
      for cb in callbacks:
        if not callable(cb):
          raise ValueError("callbacks expects callables" \
              " but found {:s}".format(repr(callbacks)))
        evs = self._indextypes['callbacks']
        while event in evs:
          if event not in accum:
            accum.append(event)
    for event in accum:
      if not event.istriggered(event, self, *args, **kwargs):
        continue
      occurs = 1
      if type(event.occurs):
        event.occurs -= 1
        occurs = event.occurs
      for cb in event.callbacks:
        if StopPropagation is cb(self._parent, event, *args, **kwargs):
          return
      if occurs <= 0:
        self.remove(events=event)
  
  def on(self, eventtype, callback, options={}, occurs=None
      , *extras, **kwextras):
    self.add( Event(eventtype, callback, options={}, occurs=None
      , *extras, **kwextras) )
  
  def once(self, eventtype, callback, options={}, *extras, **kwextras):
    self.add( Event(eventtype, callback, options={}, occurs=1
      , *extras, **kwextras) )
