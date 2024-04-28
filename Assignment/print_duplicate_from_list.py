list1=[10,53,65,10,53,69,34,75]
ulist=[]
duplist=[]

for i in list1:
    if i not in ulist:
        ulist.append(i)
    else:
        duplist.append(i)

print(ulist)