class main:
    def get(s,a,b):
        s.a=a
        s.b=b
    def dis(s):
         print("a=",s.a,"b=",s.b,"addition",s.a+s.b)
m=main()
m.get(10,20)
m.dis()
