'''#fibonacci series

n = int(input())
a ,b =0,1
for i in range(n):
    print(a,end=" ")
    a,b = b,a+b

n = int(input())
res =[0,1]
for i in range(2,n):
    res.append(res[i-1]+res[i-2])
for i in res:
    print(i,end=" ")
    '''


#power of number series
n = int(input())
for i in range(1,n+1):
    print(2**i,end=" ")