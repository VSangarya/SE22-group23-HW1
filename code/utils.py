"""
Contain utility methods
"""

import re
import csv
from globals import the

def IsInt(s):
  return re.match(r"[-+]?\d+$", s) is not None

def IsFloat(s):
  return re.match(r"[-+]?\d+\.\d+$", s) is not None

def Coerce(value):
  if IsInt(value):
    return int(value)
  elif IsFloat(value):
    return float(value)
  elif value in ("true", "True"):
    return True
  elif value in ("false", "False"):
    return False
  else: return value

def read_csv(csv_path):
  ret_rows = []
  with open(csv_path, 'r') as f:
    rows = csv.reader(f, delimiter=the["Seperator"])
    rows = [[Coerce(item) for item in eachRow] for eachRow in rows]
    for eachRow in rows:
        ret_rows.append(eachRow)
  return ret_rows

"""
def read_csv(csv_path):
    with open(csv_path) as f:
        col_name = f.readline().strip('\n').split(",")
        data = [dict(zip(col_name, i)) for i in csv.reader(f)]

    dict_cols = {i:[c[i] for c in data] for i in col_name}

    index = [idx for idx, s in enumerate(col_name) if ':' in s][0]
    dict_cols.pop(col_name[index])
    col_name.pop(index)
    for key, val in dict_cols.items():
        dict_cols[key] = list(map(float, val))
    return dict_cols, col_name
"""

def push(t,x):
  t.append(x)
  return  
def copy(t):
  t_copy=[]
  if type(t)!='list':
    return t
  else:
    for i in range(len(t)):
      t_copy.append(t[i])
