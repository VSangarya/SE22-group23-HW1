class Sym:
    n = 0
    at = 0
    name = ""
    has = {}
    summary = {}

    def __init__(self, name, index):
        self.name = name
        self.at =  index

    def add(self, v):
        if v != "?":
            self.n = self.n + 1

            if v in self.has:
                self.has[v] += 1
            else:
                self.has[v] = 1

    def mid(self):
        mode = -1
        most = ""
        for k,v in self.has.items():
            if v > mode :
                mode = v
                most = k
        return mode


    def __repr__(self):
        self.summary["n"] = self.n
        self.summary["at"] = self.at
        self.summary["name"] = self.name
        self.summary["data"] = self.has
        return str(self.summary)
