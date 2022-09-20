import Sym
import Num
import Data
from random import seed
from globals import the, fails
from utils import read_csv

class Tests:
    tests = ["bad", "ls", "all", "the", "sym", "nums", "bignum", "csv", "data", "stats"]

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
        data = read_csv("../data/test.csv", lambda row : row)
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
        d = Data.Data("../data/test.csv")        
        for a in d.cols.y:
            print(a.__repr__())
        return True

    def stats(self):
        d = Data.Data("../data/test.csv")
        print("xmid", d.stats(2, d.cols.x, "mid"))
        print("xdiv", d.stats(3, d.cols.x, "div"))
        print("ymid", d.stats(2, d.cols.y, "mid"))
        print("ydiv", d.stats(3, d.cols.y, "div"))
        return True

    def stats(self):
        d = Data.Data("../data/test.csv")
        print("xmid", d.stats(2, d.cols.x, "mid"))
        print("xdiv", d.stats(3, d.cols.x, "div"))
        print("ymid", d.stats(2, d.cols.y, "mid"))
        print("ydiv", d.stats(3, d.cols.y, "div"))
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
        if(out):
            print("Test {} PASSED!!!\n".format(test))
        else:
            print("Test {} FAILED!!!\n".format(test))
        return out == True
