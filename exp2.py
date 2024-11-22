# linear search
list = list()
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1
n = int(input("enter no,of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list.append(element)

target = int(input("Enter the target element to search for: "))
result = linear_search(list, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

'''# bubble sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Input number of elements
n = int(input("Enter number of elements: "))

# Input the elements
arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Sorting the array
bubble_sort(arr)

# Output the sorted array
print("Sorted array:", arr)'''
