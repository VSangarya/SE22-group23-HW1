import Sym
import Num
from random import seed
from globals import the
from utils import read_csv

class Tests:
    def the(self):
        return len(globals.the.keys()) > 0            

    def csv(self):        
        data = read_csv("../data/test.csv")
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
        return 32==len((num2.has))
    
    def sym(self):
        sym=Sym.Sym(0,'a')
        list_obj=['a', 'a', 'a', 'a', 'b', 'b', 'c' ]
        for i in list_obj:
            sym.add(i)
        mode=sym.mid()
        entropy=sym.div()
        print("{}\t{}".format(mode, entropy))
        return mode=="a" and entropy>=1.37 and entropy<=1.38

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
