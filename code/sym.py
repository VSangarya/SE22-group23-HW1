"""
Module for Sym class
"""

import math

class Sym:
  """Class Sym"""
  n = 0
  at = 0
  name = ""
  has = {}
  summary = {}

  def __init__(self, index, name):
    self.at = index
    self.name = name

  def Add(self, v):
    if v != "?":
      self.n = self.n + 1

      if v in self.has:
        self.has[v] += 1
      else:
        self.has[v] = 1

  def Mid(self):
    most = -1
    mode = ""
    for k, v in self.has.items():
      if v > most:
        most = v
        mode = k
    return mode

  def Div(self):
    e = 0
    for _, value in self.has.items():
      if value > 0:
        e = e - (value/self.n)*math.log(value/self.n, 2)
    return e

  def __repr__(self):
    self.summary["n"] = self.n
    self.summary["at"] = self.at
    self.summary["name"] = self.name
    self.summary["data"] = self.has
    return str(self.summary)
