''' input:4
output:
* * * *
* * * *
* * * *
* * * *

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()


#input:4
output: 
* 
* * 
* * *
* * * *
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
#input:4
#output:
* * * *
* * *
* * 
*
n = int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*",end=" ")
    print()
#n=4
A
A B
A B C D 

#n = 4 
* * * *
*     *
*     *
* * * *
#n = 4
1
2 3
4 5 6
7 8 9 10
staircase hacckerrank

n = int(input())
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
    '''