import math
from random import randrange, uniform
from globals import the

class Num:
    n =0
    at =0
    name =""
    has =[]
    lo =math.inf
    hi =-math.inf
    issorted =False
    weight =0
    summary = {}

    def __init__(self, index, name):
        self.at =index
        self.name =name
        self.has = []

    def Nums(self):
        self.has.sort()
        self.issorted =True        

    def Add(self,v):
        if v != "?":
            
            self.n = self.n + 1
            self.lo =min(self.lo, v)
            self.hi =max(self.hi, v)
            pos =None
            
            if len(self.has)<the["nums"]:                
                pos=len(self.has)
                self.has.append(None)
            elif uniform(0,1)< the["nums"]/self.n:                
                pos=randrange(0,len(self.has))
            if pos is not None:
                self.issorted = False
                self.has[pos]= int(v)

    def percentile(self,data, perc):
        size = len(data)
        return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]

    def Div(self):
        self.Nums()
        std = (self.percentile(self.has,90) -self.percentile(self.has, 10))/2.58
        return std

    def Mid(self):
        self.Nums()
        med = self.percentile(self.has, 50)
        return med

    def __repr__(self):
        self.summary["n"] = self.n
        self.summary["at"] = self.at
        self.summary["name"] = self.name        
        self.summary["lo"] = self.lo
        self.summary["hi"] = self.hi
        self.summary["issorted"] = self.issorted
        self.summary["weight"] = self.weight
        return str(self.summary)