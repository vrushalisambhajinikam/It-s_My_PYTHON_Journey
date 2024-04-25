list1=[10,53,65,10,53,69,34,75]
print(list1)
print("\n")
temp=list1[0]
for i in list1:
    if temp==i:
        list1.remove(i)
    temp=list(i+1)
    print(temp)

print(list1)