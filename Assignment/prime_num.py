def checkprime():
    num1=int(input("Enter your number : "))
    for i in range(2,num1):
        if num1%i==0:                           #9
          return 0
        break
        
    return 1
    


ans=checkprime()
if ans==1:
   print("Prime number")
else:
   print("Not Prime number")