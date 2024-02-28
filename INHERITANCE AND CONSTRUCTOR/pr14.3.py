class square:
    def method(self,length,breadth):
        self.length=length
        self.breadth=breadth
       
        print("area of rectangle",(self.length*self.breadth))
        
class rectangle:
    def method(self,side):
        self.side=side
        print("value of b",self.side)
        print("area of square",(self.side*self.side))

a1=square()        
a2=rectangle()
a1.method(10,4)
a2.method(4)


    
        
        
