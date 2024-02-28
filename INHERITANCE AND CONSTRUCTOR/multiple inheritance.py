class single:
    def getdata(self):
        print("hello")
class derived1:
    def dis(self):
        print("derived")
class derived2(derived1,single):
    def dis2(self):
        print("hello multilevel")
d=derived2()
d.getdata()
d.dis()
d.dis2()
    
