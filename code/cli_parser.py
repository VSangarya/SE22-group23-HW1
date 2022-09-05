"""
Methods that deal with parsing command-line options
"""

import sys
from utils import IsInt, IsFloat

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

def Cli(d):
  for option, value in d.items():
    value = str(value)
    i = 1
    # len(sys.argv) - 1 because sys.argv[0] contains name of the invoked script
    while i <= (len(sys.argv) - 1):
      if (sys.argv[i] == "".join(["-", option[:1]]) or
          sys.argv[i] == "".join(["--", option])):
        if value == "True":
          value = "False"
        elif value == "False":
          value = "True"
        else:
          value = sys.argv[i+1]
          i = i + 1   # increment i to skip reading next argument!
      i = i + 1
    d[option] = Coerce(value)