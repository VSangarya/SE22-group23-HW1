"""Definition for Cols"""

import re
import sym
import num

class Cols:
  """Class Cols"""
  def __init__(self, names):
    self.names = names
    self.all = []
    self.klass = None
    self.x = []
    self.y = []
    for key, value in enumerate(names):
      obj = None
      m = re.search(r'^[A-Z]+', value)
      if m:
        obj = num.Num(key, value)
      else:
        obj = sym.Sym(key, value)

      self.all.append(obj)

      if not re.search(r':$', value):
        if re.search(r'[!\+\-]', value):
          self.y.append(obj)
        else:
          self.x.append(obj)
        if re.search(r'!$', value):
          self.klass = obj
