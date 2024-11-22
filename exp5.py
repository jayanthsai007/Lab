# Mean
'''import numpy
l = []
n = int(input(f"enter value of n: "))
for i in range(n):
    l.append(int(input(f"enter value {i+1}: ")))
mean = (sum(l)/n)
print(f"mean is: {mean}")'''
# Median
'''list = []
n = int(input(f"Enter value of n: "))
for i in range(n):
    list.append(int(input(f"Enter value {i+1}: ")))
list.sort()
mid_val = len(list)//2
result = (list[mid_val] + list[~mid_val])/2
print(f"Median of list is : {result}")'''
# mode
d = {}
list = [10, 10, 30]
max_occur = 0
for i in list:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        max_occur = max(max_occur, d[i])
    if max_occur == 1:
        print("no mode found")
    else:
        list1 = [i for i in d if d[i] == max_occur]
        print(f"mode is: {list1}")
