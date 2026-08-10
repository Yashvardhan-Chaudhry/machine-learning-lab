import numpy as np
np.set_printoptions(precision=1, floatmode='fixed')
""" Q3: Based on Searching and Sorting
(a) For the array: array = np.array([10, 52, 62, 16, 16, 54, 453]), find 
i.  Sorted array 
ii.  Indices of sorted array 
iii.  4 smallest elements 
iv.  5 largest elements 
(b) For the array: array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0]), find 
i.  Integer elements only 
ii.  Float elements only  """
print("---Part (a)---")
array = np.array([10, 52, 62, 16, 16, 54, 453])
print(f"Working array:\n{array}")
def sort(arr):
    sorted_array=np.sort(arr)
    print(f"Sorted array:\n{sorted_array}")
    print(f"Indices :\n{np.argsort(arr)}")
    print(f"iii. 4 smallest elements:{sorted_array[:4]} ")
    print(f"iv. 5 largest element: {sorted_array[-1:-6:-1]}")
sort(array)
print("---Part(b)---")
array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
def part_b(arr):
    arr1=np.where(arr==np.floor(arr))
    arr2=np.where(arr!=np.floor(arr))
    arr_int=arr[arr1]
    arr_float=arr[arr2]
    print(f"Array with integer only elements: {arr_int}")
    print(f"Array with float only elements: {arr_float}")

print(f"Working array:{array}")
part_b(array)