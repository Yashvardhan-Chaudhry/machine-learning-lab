#(a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5])
import numpy as np
# arr = np.array([1, 2, 3, 6, 4, 5])
# newarr=arr[::-1]
# print("Original Array: ", arr)
# print("Reversed array: ",newarr)
# #(b) Flatten the NumPy arr: array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]]) using any two 
# #NumPy in-built methods 
# array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
# array1_flattened=array1.reshape(-1)
# print("Original Array: ", array1)
# print("Flattened Array: ", array1_flattened)
#(c)Compare the following numpy arrays: 
#arr1 = np.array([[1, 2], [3, 4]]) 
#arr2 = np.array([[1, 2], [3, 4]])
# arr1 = np.array([[1, 2], [3, 4]]) 
# arr2 = np.array([[1, 2], [3, 4]])
# flag=False
# for i in np.nditer([arr1,arr2]):
#     if (i[0]!=i[1]):
#         flag=True
#         break
# if flag:
#     print("Arrays are not equal")
# else:
#     print("Arrays are equal")
# (d) Find the most frequent value and their indice(s) in the following arrays: 
# i.  x = np.array([1,2,3,4,5,1,2,1,1,1]) 
# ii.  y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
x = np.array([1,2,3,4,5,1,2,1,1,1]) 
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
def q1_d(arr):
    uniqueVals,count= np.unique(arr,return_counts=True)
    most_frequent=(uniqueVals[count==count.max()])

    for i in most_frequent:
        indices=np.where(i==arr)
        print(f"The most frequent value is/are : {i} and its indices: {indices}")

def q1_d_loop(arr):
    uniqueVals=np.unique(arr)
    maxCount=0
    most_frequent=[]
    for i in uniqueVals:
        count=0
        for j in arr:
            if j==i:
                count=count+1
        if count==maxCount:
            maxCount=count
            most_frequent.append(i)
        elif count>maxCount:
            maxCount=count
            most_frequent=[]
            most_frequent.append(i)
    for i in most_frequent:
        indices=np.where(arr==i)
        print(f"The most frequent value is/are : {i} and its indices: {indices}")

q1_d(x)
q1_d(y)
q1_d_loop(x)
q1_d_loop(y)