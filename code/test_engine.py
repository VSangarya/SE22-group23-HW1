import Sym
import Num
import Data
from random import seed
from globals import the
from utils import read_csv

class Tests:
    def the(self):
        return len(globals.the.keys()) > 0            

    def csv(self):        
        data = read_csv("data/test.csv", lambda row : row)
        for o in data[:12]:
            print(o)
        return True

    def nums(self):
        num=Num.Num(0,'a')       
        for i in range(1,101):
            num.Add(i)        
        mid=num.Mid()
        div=num.Div()
        print("{}\t{}".format(mid, div))
        return 50<=mid and mid<=52 and 30.5<div and div<32

    def bignum(self):
        num2=Num.Num(1,'b')      
        the["nums"]=32        
        for i in range(1,1001):            
            num2.Add(i)
        num2.Nums()
        print(num2.has)
        seed(the["seed"])
        return 32==len((num2.has))
    
    def sym(self):
        sym=Sym.Sym(0,'a')
        list_obj=['a', 'a', 'a', 'a', 'b', 'b', 'c' ]
        for i in list_obj:
            sym.Add(i)
        mode=sym.Mid()
        entropy=sym.Div()
        print("{}\t{}".format(mode, entropy))
        return mode=="a" and entropy>=1.37 and entropy<=1.38

    def data(self):
        d = Data.Data("data/test.csv")        
        for a in d.cols.y:
            print(a.__repr__())
        return True

    def stats(self):
        d = Data.Data("data/test.csv")
        print("xmid", d.stats(2, d.cols.x, "mid"))
        print("xdiv", d.stats(3, d.cols.x, "div"))
        print("ymid", d.stats(2, d.cols.y, "mid"))
        print("ydiv", d.stats(3, d.cols.y, "div"))
        return True

    def runs(self):
        seed(the["seed"])
        if self.sym():
            print("SYM PASSED\n")
        else:
            print("SYM FAILED\n")
        if self.nums():
            print("NUMS PASSED\n")
        else:
            print("NUMS FAILED\n")
        if self.bignum():
            print("BIGNUM PASSED\n")
        else:
            print("BIGNUM FAILED\n")
        if self.csv():
            print("CSV PASSED\n")
        else:
            print("CSV FAILED\n")
        if self.stats():
            print("STATS PASSED\n")
        else:
            print("STATS FAILED\n")
        if self.data():
            print("DATA PASSED\n")
        else:
            print("DATA FAILED\n")
