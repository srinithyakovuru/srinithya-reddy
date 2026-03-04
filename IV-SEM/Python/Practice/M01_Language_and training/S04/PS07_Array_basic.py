'''
import array
arr=array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.insert(1, 12)
print(arr)
'''

'''
List:
1.list is Mutable
2.list allows duplicate values
3.list can store different data types
4.list is defined using []
5.list is heterogeneous
6.list is indexed
'''
'''li=[12,25.4,6+5j,"nithya",12,25.4]
print(li,type(li))
print(li[3])
print(li[3:6:1])
print(li[::-1])
print(len(li))
li.append(100)
print(li)
li.insert(2,"hello")
print(li)
'''
'''Array:
1.array is Mutable
2.array allows duplicate values
3.array can store only same data types
4.array is defined using array module
5.array is homogeneous
6.array is indexed
'''
'''#Read a number from user and display no.of digits in that number
input:1234
output:4
n=int(input("Enter a number:"))
count=0
while n>0:
    n=n//10
    count=count+1
    print(count)
    '''
'''
NUMPY: 
Numpy->Numerical Python  '''
import numpy as np
arr=np.array([10,20,30,40,50])
print("Array elements are:",arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))     
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(5))
print("Even numbers are:",np.arange(2,10,2))
print("Odd numbers are:",np.arange(1,10,2))

n=int(input("Enter size of array:"))
ele=list(map(int,input("Enter elements:").split()))
print("Array elements are:",np.array(ele))


