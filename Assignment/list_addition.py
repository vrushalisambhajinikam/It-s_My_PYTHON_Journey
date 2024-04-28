l1=[]

size=int(input("Enter how many list ele you want to store:"))
print("Enter list element : ")
for i in range(size):
    ele=input("Enter ele : ".format(i+1))
    l1.append(ele)

print(l1)

s1=''
for i in l1:
    s1=s1+str(i)

print(s1)
