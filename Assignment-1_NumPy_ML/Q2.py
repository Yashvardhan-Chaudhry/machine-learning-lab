import numpy as np
""" Q2: Based on NumPy Mathematics and Statistics 
(a)  For the array: array = np.array([[1, -2, 3],[-4, 5, -6]]) 
i.  Find element-wise absolute value 
ii.  Find the 25th, 50th, and 75th percentile of flattened array, for each column, for each 
row. 
iii.  Mean, Median and Standard Deviation of flattened array, of each column, and 
each row 
(b)  For the array: a = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0]). Find floor, ceiling 
and truncated value, rounded values  """
print("Q2: Based on NumPy Mathematics and Statistics ")
def element_abs(arr):
    print(f"element wise absolute value:\n{np.abs(arr)}")
array = np.array([[1, -2, 3],[-4, 5, -6]]) 
print(f"Given array for computation:\n{array}")
element_abs(array)
def percentile(arr):
    q=[25,50,75]
    print("---Flattened array---")
    arr1=arr.reshape(-1)
    for i in q:
        print(f"{i}th percentile for array: {np.percentile(arr1,i)}")
    print("---Coloumn-wise---")
    for i in q:
        print(f"{i}th percentile for each coloumn: {np.percentile(arr,i,axis=0)}")
    print("---Row-Wise---")
    for i in q:
        print(f"{i}th percentile for each row: {np.percentile(arr,i,axis=1)}")
percentile(array)
def mean_median_sd(arr):
    arr1=arr.reshape(-1)
    print("---Flattened array---")
    print(f"Mean:{np.mean(arr1)} ")
    print(f"Median:{np.median(arr1)}")
    print(f"Standard Deviation: {np.std(arr1)}")
    print("---Column-wise---")
    print(f"Mean: {np.mean(arr,axis=0)}")
    print(f"Median: {np.median(arr,axis=0)}")
    print(f"Standard deviation: {np.std(arr,axis=0)}")
    print("---Row-wise---")
    print(f"Mean: {np.mean(arr,axis=1)}")
    print(f"Median: {np.median(arr,axis=1)}")
    print(f"Standard deviation: {np.std(arr,axis=1)}")
mean_median_sd(array)
a = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0])
def part_b(a):
    print(f"Given array:\n {a}") #floor, ceiling and truncated value, rounded values
    print(f"Floored: {np.floor(a)}")
    print(f"Ceiled: {np.ceil(a)}")
    print(f"Truncated: {np.trunc(a)}")
    print(f"Rounded: {np.round(a)}")
part_b(a)

