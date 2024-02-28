class InvalidPasswordException(Exception):
    pass
try:
   password=int(input("Enter password"));
   if password>6:
     raise InvalidPasswordException("invalid password");
   else:
       print("valid password")
        
except InvalidPasswordException as b:
    print(b);
  
