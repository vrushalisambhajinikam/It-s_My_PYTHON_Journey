class single:
    def getdata(self):
        self.id=int(input("enter id"))
        self.name=(input("enter name"))
class derived1(single):
    def dis(self):
        print("id=",self.id)
        print("name=",self.name)
class derived2(derived1):
    def dis2(self):
        print("hello multilevel")
d=derived2()
d.getdata()
d.dis()
d.dis2()
    
