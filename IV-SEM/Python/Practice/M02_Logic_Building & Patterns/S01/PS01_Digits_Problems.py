# n = int(input())
# n = str(n)
# print(len(n))
'''
# no of digits in a number
n = int(input())
count = 0
while n>0:
    count+=1
    n = n//10
print(count)
'''
'''
#sum of digits in a number
n = int(input())
temp = n
s = 0 
while n>0:
    last = n%10
    s = s+last
    n = n//10
print(s)

#print(sum(map(int,str(temp))))

#count of even and odd digits in a number
n = int(input())
even = 0
odd = 0
while n>0:
    if n%2==0:
        even+=1
    else:
        odd+=1
    n = n//10
print(even,odd)


#digital root sum of digits until we get a single digit
n = int(input())
sum = 0
while n>0:
    sum = sum + n%10
    n = n//10
while sum>9:
    sum = sum%10 + sum//10
print(sum)

#n = int(input())
while n>9:
    n = sum(map(int,str(n)))
print(n)
'''
#display te reverse of a number
n = int(input())
last = 0

n = int(input())
n = str(n)
print(n[::-1])