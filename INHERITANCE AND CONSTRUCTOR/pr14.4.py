class Degree:
    def getdegree(self):
        print("I got a degree")
class Undergraduate(Degree):
    def method(self):
        print("I am an Undergraduate")
class Postgraduate(Degree):
    def method(self):
        print("I am an Postgraduate")

d=Degree()
u=Undergraduate()
p=Postgraduate()
d.getdegree()
u.method()
p.method()
        
