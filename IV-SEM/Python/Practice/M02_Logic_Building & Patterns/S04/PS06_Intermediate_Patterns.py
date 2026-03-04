'''
#1.traditinal method for doubling the numbers
li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i*2)
print(res)
# list comprehension method
print([i*2 for i in li])

#2.inding even numbers in a list
li = [1,2,3,4,5]
res = []
for i in li:
    if i%2==0:
        res.append(i)
print(res)
 
#with list comprehension 
print([i for i in li if i%2==0])

#3.traditional metod of joining 
li = ['a','b','c']
str = ""
for i in li:
    str+=i 
print(str)
#using join method
print("".join(li))
'''
'''Intermediate patterns
1. Pyramid
n = 4
output:
    *
   * *
  * * *
 * * * *

n = int(input())
for i in range(1,n+1):
    print((n-i)*" "+i*"* ")
'''
'''
inverted pyramid
#n = 4
#output:
* * * * 
 * * * 
  * * 
   * 

n = int(input())
for i in range(1,n+1):
    print(" "*(i-1)+"* "*(n-i+1))
#or
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

n = int(input())
for i in range(1,n+1):
    print((n-i)*" "+i*"* ")
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
#output:
#    * 
#   * * 
#  * * * 
# * * * * 
#  * * * 
#   * * 
#    * 

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))
# output:
#    1
#   1 2
#  1 2 3
# 1 2 3 4

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(i) for j in range(1,i+1)]))
# output:
#    1
#   2 2
#  3 3 3
# 4 4 4 4

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([chr(64+j) for j in range(1,i+1)]))
# output:
#    A
#   A B
#  A B C
# A B C D

n = int(input())
val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(val),end=" ")
        val+=1
    print()
# output:4
# A 
# B C 
# D E F 
# G H I J 

6. Reverse Number Triangle
n=4
Output:
1 2 3 4
1 2 3
1 2
1

n = int(input())
for i in range(n,0,-1):
    num = 1
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()

    7. Binary Triangle
n=4
Output:
1
0 1
1 0 1
0 1 0 1

n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print() 

8. Cross Pattern
n=5``
Output:
*       *
  *   *
    *
  *   *
*       *

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    9. Hollow Diamond
n=4
Output:
   *
  * *
 *   *
*     *
 *   *
  * *
   * '''