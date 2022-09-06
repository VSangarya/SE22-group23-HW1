"""
Stitches different modules together (main file)
"""

import re
import sys
from random import seed
from globals import the
from cli_parser import Coerce, Cli
from test_engine import Tests

# helper string
help_str = """CSV : summarized csv file

USAGE: python main.py [OPTIONS]

OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --Seperator feild seperator                       = ,
"""

default_values = re.findall(
                  r"\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)", help_str)
for option, value in default_values:
  the[option] = Coerce(value)

# parse user-defined options
Cli(the)

# print help and exit if option 'help' is invoked
if the["help"]:
  print(help_str)
  sys.exit(0)

seed(the["seed"])

t=Tests()

if t.sym():
    print("SYM PASSED\n")
else:
    print("SYM FAILED\n")

if t.nums():
    print("NUMS PASSED\n")
else:
    print("NUMS FAILED\n")


if t.bignum():
    print("BIGNUM PASSED\n")
else:
    print("BIGNUM FAILED\n")