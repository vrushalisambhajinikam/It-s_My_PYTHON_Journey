dict={'name':'zara','age':7,'class':'first'}
print(dict);

print(dict['name'])
print(dict['age'])
print(dict['class'])

dict['name']="vibha"
print(dict['name'])

print(dict);

#del dict['name']
print(dict);

#del dict
print(dict);

#dict.clear()
print(dict);


for key,value in dict.items():
    print(key,"-",value)
