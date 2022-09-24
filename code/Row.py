"""
Definition for Row class
"""

import utils

class Row:
  """Class Row"""
  cells=None
  cooked=None
  is_evaled=False
  metatable=None

  def __init__(self,t):
    self.cells=t
    self.cooked=utils.copy(t)
    self.is_evaled=False

  def get_metatable(self):
    return self.metatable

  def set_metatable(self,u):
    self.metatable=u
