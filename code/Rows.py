from re import T


import utils

class Rows:
    cells=None
    cooked=None
    isEvaled=False
    metatable=None

    def __init__(self,t):
        self.cells=t
        self.cooked=utils.copy(t)
        self.isEvaled=False

    def get_metatable(self):
        return self.metatable
        
    def set_metatable(self,u):
        self.metatable=u