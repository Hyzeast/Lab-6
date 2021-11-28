class sst(str):
    def _init(self,ss):
        self.s=str(ss)
    def find3(self,x):
        self.s=x
    def palindrom1(self):
        x=self.s
        L=len(x)
        indicator=True
        for i in range(L):
            if x[i]!=x[L-i-1]:
                indicator=False
            return (indicator)
    def palindrom2(self,x):
        self.s=str(x)
        L=len(x)
        indicator=True
        for i in range(L):
            if x[i]!=x[L-i-1]:
                indicator=False
        return (indicator)
    def read_s(self):
        self.s=input("Введіть рядок")
sss=input("?????")
y=sst()
y._init(sss)
print(y.palindrom2(sss))
y.read_s()
print(y.palindrom1())  