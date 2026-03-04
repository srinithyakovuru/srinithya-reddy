'''#running sum
nums = list(map(int,input().split()))
sum1 = 0
res = []
for i in range(len(nums)):
    sum1 +=nums[i]
    res.append(sum1)
print(res)
# input:1 2 3 4 5
# output:[1, 3, 6, 10, 15]
#duplicates
arr = list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]!=arr[i+1]:
        print("false")
    else:
        print("true")
Sets:
1) Definition: A set is an unordered collection of unique elements. It is defined using curly braces {} or the built-in set() function.
2) Creation : set()
3)Adding: add() method is used to add an element to a set. If the element already exists, it will not be added again, as sets do not allow duplicates.
4) Removing: remove() method is used to remove an element from a set. If the element does not exist, it raises a KeyError. The discard() method can also be used to remove an element, but it does not raise an error if the element is not found.
5) Set Operations: union,intersection,difference,symmetric_difference
'''
a = set([1, 2, 3, 4, 5])
print(a)
a.add(6)
a.add(5)
a.remove(3)
print(a)
b = set([4, 5, 6, 7, 8])
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))