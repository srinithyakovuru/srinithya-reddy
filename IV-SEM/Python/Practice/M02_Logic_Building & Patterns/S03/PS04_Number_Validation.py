'''
#check if the number is Armstrong number:
input : 153
output : Armstrong

input: 24
output: Not Armstrong

n = int(input())
a = len(str(n))
sum = 0
for i in str(n):
    sum+=int(i)**a
print("Armstrong" if sum==n else "Not Armstrong")

#check whether the number is perfect number
# input: 6 output: perfect number 
n = int(input())
sum =0
for i in range(1,n//2+1):
    if n%i ==0:
        sum+=i 
print("perfect number" if sum==n else "Not a perfect number")

#check whether the number is strong number or not
def factorial(n):
    if n<0:
        return "Factorial not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact*=i
        return fact


n = int(input())
sum =0
for i in str(n):
    sum+=factorial(int(i))
print("strong number" if sum==n else "not a strong number")
'''
#if the number is not palindrome reverse it and to the number again check the condition
n = int(input())
a = str(n)
if a[::-1]==n:
    print("palindrome")