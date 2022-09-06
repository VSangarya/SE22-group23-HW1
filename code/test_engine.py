import Sym
import Num
import globals
class Tests:
    def the(self):
        if len(globals.the.keys())>0:
            print("Global Variables are set! \n PASSED!!!!\n\n")
        else:
            print("Global variables not set \n FAILED\n\n")

    def nums(self):
        num=Num.Num(0,'a')       
        for i in range(1,101):
            num.Add(i)        
        mid=num.Mid()
        div=num.Div()
        print(mid, div)
        return 50<=mid and mid<=52 and 30.5<div and div<32

    def bignum(self):
        num2=Num.Num(1,'b')      
        globals.the["nums"]=32        
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
        print(mode, entropy)
        return mode=="a" and entropy>=1.37 and entropy<=1.38
