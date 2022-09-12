import re
import Sym
import Num

class Cols:
    def __init__(self,names):
        self.names = names
        self.all ={}
        self.klass = None
        self.x = {}
        self.y = {}
        for key,value in names.items():
            col = {}
            x = None
            if(re.match("(^[A−Z]*)",value) is None): 
                x = Sym(key,value) 
            else: 
                x = Num(key,value)
            col = self.all.append(x)
            if(re.match(":$",value) is None):
                if(re.match("[!+−]",value) is None):
                    col.append(self.x)
                else:
                    col.append(self.y)
            else:
                self.klass = col
    
    





