def checkdigit():
    ch1=(input("Enter your character : "))
    if(ch1 >'0' and ch1<'9'):
       return 1
    else:
       return 0
    
ans=checkdigit()
if ans==1:
   print("Given value os digit")
else:
   print("Given value is character")