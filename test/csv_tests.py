from class import sym
from class import Num
class Tests:
    def the(self,the_object):
        if the_object:
            print("Global Variables are set! \n PASSED!!!!")
    
    def nums(self):
        for i in range(1,101):
            num.add(i)
        num=Num()
        mid=num.mid()
        div=num.div()
        print(mid,div)
        return 50<=mid and mid<=52 and 30.5<div and div<32

    def bignum(self):
        num=Num()
        the.nums=32
        for i in range(1,1001):
            num.add(i)
        print(num.nums())
        return 32==len(list(num.has))
    
    def sym(self):
        sym=Sym()
        list_obj=['a', 'a', 'a', 'a', 'b', 'b', 'c' ]
        for i in list_obj:
            sym.add(i)

        mode=sym.mid()
        entropy=sym.div()
        entropy=(entropy*1000)//1*1000
        print(mode, entropy)
        return mode=="a" and entropy>=1.37 and entropy<=1.38

        