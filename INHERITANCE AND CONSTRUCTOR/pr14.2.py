class print1:
   def method(self,n,c):
       self.n=n
       self.c=c
       print("integer=",self.n)
       print("character=",self.c)
class print2:
   def method(self,c,n):
       self.c=c
       self.n=n
       print("character=",self.c)
       print("integer=",self.n)
p1=print1()
p2=print2()
p1.method(10,"hello")
p2.method("hr",100)
