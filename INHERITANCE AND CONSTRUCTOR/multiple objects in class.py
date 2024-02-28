class student:
    def get(self):
        self.rollno=int(input("enter rollno"))
        self.name=(input("enter name"))
        self.marks=float(input("enter marks"))
    
    def dis(self):
        print("rollno of student:",self.rollno)
        print("name of student:",self.name)
        print("marks of student:",self.marks)
s1=student()
s2=student()
s1.get()
s2.get()
s1.dis()
s2.dis()
