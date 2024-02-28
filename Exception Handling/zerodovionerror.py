a=1;
b=0;
try:
  print(a/b);
except:
    ZeroDivisionError:print("zero division error occur");
finally:
    print("always excuted");
