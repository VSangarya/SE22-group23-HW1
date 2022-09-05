"""
Contain utility methods
"""

import re
import csv

def IsInt(s):
  return re.match(r"[-+]?\d+$", s) is not None

def IsFloat(s):
  return re.match(r"[-+]?\d+\.\d+$", s) is not None




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