"""Definition for data"""

from utils import is_float, read_csv, rnd
import cols
import row


class Data:
  """Class Data"""
  rows = []
  cols = []

  def __init__(self, src):
    self.cols = []
    self.rows = []
    if isinstance(src, str):
      read_csv(src, self.Add)
    else:
      for _, i_row in src.items():
        self.Add(i_row)

  def Add(self, xs):
    if not self.cols:
      self.cols = cols.Cols(xs)
    else:
      r = row.Row(xs)
      self.rows.append(r)
      for col in [*self.cols.x, *self.cols.y]:
        col.Add(r.cells[col.at])

  def Stats(self, places, show_col, fun):
    t = {}
    for col in show_col:
      v = None
      if fun == "mid":
        v = col.Mid()
      elif fun == "div":
        v = col.Div()

      if is_float(str(v)):
        v = rnd(v, places)

      t[col.name] = v
    return t
