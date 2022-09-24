"""Defines for test engine"""
import sym
import num
import data
from random import seed
from globals import the, fails
from utils import read_csv


class Tests:
  "Class definition for test engine"
  tests = ["bad", "ls", "all", "the", "sym",
       "nums", "bignum", "csv", "data", "stats"]

  def bad(self):
    return True

  def ls(self):
    print("Examples:\nlua csv -e ...")
    for item in sorted(self.tests):
      print(item)
    return True

  def the(self):
    return len(the.keys()) > 0

  def csv(self):
    items = read_csv("../data/test.csv", lambda row: row)
    for o in items[:12]:
      print(o)
    return True

  def nums(self):
    n = num.Num(0, "a")
    for i in range(1, 101):
      n.Add(i)
    mid = n.Mid()
    div = n.Div()
    print(f"{mid}\t{div}")
    return 50 <= mid <= 52 and 30.5 < div  < 32

  def bignum(self):
    num2 = num.Num(1, "b")
    the["nums"] = 32
    for i in range(1, 1001):
      num2.Add(i)
    num2.Nums()
    print(num2.has)
    seed(the["seed"])
    return 32 == len((num2.has))

  def sym(self):
    s = sym.Sym(0, "a")
    list_obj = ["a", "a", "a", "a", "b", "b", "c"]
    for i in list_obj:
      s.Add(i)
    mode = s.Mid()
    entropy = s.Div()
    print(f"{mode}\t{entropy}")
    return mode == "a" and entropy >= 1.37 <= 1.38

  def data(self):
    d = data.Data("../data/test.csv")
    for a in d.cols.y:
      print(a.PrintContext())
    return True

  def stats(self):
    d = data.Data("../data/test.csv")
    print("xmid", d.Stats(2, d.cols.x, "mid"))
    print("xdiv", d.Stats(3, d.cols.x, "div"))
    print("ymid", d.Stats(2, d.cols.y, "mid"))
    print("ydiv", d.Stats(3, d.cols.y, "div"))
    return True

  def all(self):
    global fails
    for f in self.tests:
      if f != "all":
        if not self.runs(f):
          fails = fails + 1
    return True

  def runs(self, test):
    if test not in self.tests:
      return
    func = getattr(Tests, test)
    out = func(self)
    if out:
      print(f"Test {test} PASSED!!!\n")
    else:
      print(f"Test {test} FAILED!!!\n")
    return out is True
