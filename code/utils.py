"""
Contain utility methods
"""

import re

def IsInt(s):
  return re.match(r"[-+]?\d+$", s) is not None

def IsFloat(s):
  return re.match(r"[-+]?\d+\.\d+$", s) is not None
