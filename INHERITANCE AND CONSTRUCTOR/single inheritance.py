class single:
    def getdata(self):
        self.id=int(input("enter id"))
        self.name=(input("enter name"))
class derived(single):
    def dis(self):
        print("id=",self.id)
        print("name=",self.name)
d=derived()
d.getdata()
d.dis()
    
