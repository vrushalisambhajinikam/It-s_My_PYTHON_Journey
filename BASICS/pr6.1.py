from operator import*

list1=[1,2,3,4]
print("",list1);
total=sum(list1);
print("sum of all elements",total);



list2=[100,200,300,50];
for p in range(0,len(list2)):
 total=total+list2[p];
print("sum of all elements=",total);



list3=[1,1,3,5];
total=1;
for l in range(0,len(list3)):
 total=total*list3[l];
print("multiplication of all elements=",total);

list4=[1,1,3,5];
total=1;
for l in list4:
  total=mul(l,total);
print("multiplication of all elements=",total);



list5=[7,2,20,10,4];
list5.sort();
print("largest no in the list:",list5[-1]);


x=max(list5);
print("largest no in the list:",x);


list5=[7,2,20,10,4];
list5.sort();
print("smallest no in the list:",list5[0]);


x=min(list5);
print("smallest no in the list:",x);




list5=[7,2,20,10,4];
list5.reverse();

print("reverse list:",list5);
print("reversed method:",list(reversed(list5)))



list6=[10,2,30,40];
list7=[100,30,20,50];

if(set(list6)&set(list7)):
    print(set(list6)&set(list7));
else:
    print("no matching ele")



def common(a,b):
    return list(set(list6)&set(list7))
e=common(list6,list7)
print(" matching ele",e)


list6=[10,2,7,30];
for ele in list6:
    if ele%2==0:
     print("even no:",ele)

    







