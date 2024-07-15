'''Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i square.'''

n = int(input())
if(n>=1):
        for i in range(n):
            print(i*i)