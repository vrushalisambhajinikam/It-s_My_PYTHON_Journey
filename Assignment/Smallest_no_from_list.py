list1=[100,56,89,23,65,41]
small=list1[0]
for i in list1:
    if small>i:
        small=i

print("Smallest number from list is: ",small)
