tupp=(10,100,55,60,70,100,60);
print(type(tupp));
print(tupp[-1]);
print(tupp[-5]);

print(tupp[1:4]);
print(tupp[:-4]);
print(tupp[4:]);
print(tupp[:]);

print(tupp.count(100));
print(tupp.index(100));

for x in tupp:
    print(x);

print(10 in tupp);
print(1000 in tupp);


print(10 not in tupp);
print(1000 not in tupp);
