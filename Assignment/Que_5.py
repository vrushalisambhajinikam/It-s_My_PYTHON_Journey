def cal(n1,n2):
    prod=n1*n2
    if prod>1000:
        return n1+n2
    else:
        return prod


n1=int(input("Enter 1st integer value: "))
n2=int(input("Enter 2nd integer value: "))

ans=cal(n1,n2)
print(ans)