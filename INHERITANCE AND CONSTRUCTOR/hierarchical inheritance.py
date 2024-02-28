class single:
    def getdata(self):
        print("hello")
class derived1(single):
    def dis(self):
        print("derived")
class derived2(single):
    def dis2(self):
        print("hello hierachical")
d1=derived1()
d2=derived2()

d1.getdata()
d1.dis()

d2.getdata()
d2.dis2()
    
