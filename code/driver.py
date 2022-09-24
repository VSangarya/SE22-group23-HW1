"""
Stitches different modules together (main file)
"""

import re
import sys
from globals import the, fails
from cli_parser import coerce, Cli
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
  the[option] = coerce(value)

# parse user-defined options
Cli(the)

# print help and exit if option 'help' is invoked
if the["help"]:
  print(help_str)
  sys.exit(0)

t = Tests()
t.runs(the["eg"])
sys.exit(fails)
