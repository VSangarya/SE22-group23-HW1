import utils
import Cols
import Row

class Data:
    row = {}
    cols = {}
    def __init__(self,src):
        self.cols = {}
        self.rows = {}
        if( type(src) == 'String'):
            csv(src, function(row) self.add(row))
        else:
            for _,row in src.items():
                self.add(row)

    def Add(self,xs,row):
        if (self.cols is None):
            self.cols = Cols(xs)
        else:
            if(xs is not None):
                row = utils.push(self.rows,xs.cells)
            elif(xs is None):
                row = utils.push(self.rows,Row(xs))
            for _,todo in {self.cols.x, self.cols.y}: 
                for _,col in todo.items():
                    col.add(row.cells[col.at])

    def Stats(self,showCols,v,places = 2,fun = "mid",t={}):
        showCols = showCols or self.cols.y
        for _,col in showCols.items():
            v=fun(col)
            v= type(v)=="number" and utils.rnd(v,places) or v
            t[col.name]=v
        return t
            

