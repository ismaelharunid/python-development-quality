

class LRUStack(list):
  
  maxsize   = None
  
  def __init__(self, initializer=None, maxsize=100):
    self.maxsize = maxsize
    if initializer is None:
      super().__init__()
    else:
      super().__init__(initializer)
  
  def __trunc__(self):
    if self.maxsize is None:
      return
    while len(self) > self.maxsize:
      self.pop(0)
  
  def __imul__(self, value):
    super().__imul__(value)
    self.__trunc__()
  
  def __iadd__(self, key, values):
    super().__iadd__(value)
    self.__trunc__()
  
  def append(self, value):
    super().append(value)
    self.__trunc__()
  
  def insert(self, key, value):
    super().insert(key, value)
    self.__trunc__()
  
  def extend(self, iterable):
    super().extend(iterable)
    self.__trunc__()


