str=input()
#pos=int(input())
#charval=input()[0]

pos,charval=input().split()

def mutate_string(str,pos,charval):

    newstr=str[:pos]+charval+str[pos+1:]

    print(newstr)


mutate_string(str,int(pos),charval)