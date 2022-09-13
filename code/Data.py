from utils import IsFloat, read_csv, rnd
import Cols
import Row

class Data:
    rows = []
    cols = []
    def __init__(self,src):
        self.cols = []
        self.rows = []
        if isinstance(src, str):
            read_csv(src, lambda row : self.Add(row))
        else:
            for _,row in src.items():
                self.Add(row)

    def Add(self, xs):
        if not self.cols:
            self.cols = Cols.Cols(xs)
        else:            
            row = Row.Row(xs)
            self.rows.append(row)            
            for col in [*self.cols.x, *self.cols.y]:
                col.Add(row.cells[col.at])

    def stats(self, places, showCol, fun):
        t = {}
        for col in showCol:
            v = None
            if fun == "mid":
                v = col.Mid()
            elif fun == "div":
                v = col.Div()
            
            if IsFloat(str(v)):
                v = rnd(v, places)

            t[col.name] = v
        return t