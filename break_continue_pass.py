
fruit=['Apple','Mongo','Banana','Orange'];
for i in fruit:
    if i == 'Mongo':
        break
    print(i)

print()

fruit2=['Apple','Mongo','Banana','Orange'];
for i in fruit:
    if i == 'Mongo':
        continue
    print(i)


print()

fruit2=['Apple','Mongo','Banana','Orange'];
for i in fruit:
    if i == 'Mongo':
        pass
    print(i)