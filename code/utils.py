"""
Contain utility methods
"""

import re
import csv
import math
from globals import the

def is_int(s):
  return re.match(r"[-+]?\d+$", s) is not None

def is_float(s):
  return re.match(r"[-+]?\d+\.\d+$", s) is not None

def coerce(value):
  if is_int(value):
    return int(value)
  elif is_float(value):
    return float(value)
  elif value in ("true", "True"):
    return True
  elif value in ("false", "False"):
    return False
  else: return value

def read_csv(csv_path,fun):
  ret_rows = []
  with open(csv_path, "r", encoding = "utf-8") as f:
    rows = csv.reader(f, delimiter=the["Seperator"])
    rows = [[coerce(item) for item in r] for r in rows]
    for r in rows:
      fun(r)
      ret_rows.append(r)
  return ret_rows

def push(t,x):
  t.append(x)

def copy(t):
  t_copy=[]
  if isinstance(t, list):
    return t
  else:
    for i in range(len(t)):
      t_copy.append(t[i])
  t.setmetatable(t_copy)

def rnd(x, places):
  mult = 10**(places or 2)
  return math.floor(x * mult + 0.5) / mult
