import numpy as np


#(a) Reverse the NumPy array: arr = np.array([1, 2, 3, 6, 4, 5])
def q1_a():
    arr = np.array([1, 2, 3, 6, 4, 5])
    newarr=arr[::-1]
    print("Original Array: ", arr)
    print("Reversed array: ",newarr)


#(b) Flatten the NumPy arr: array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]]) using any two
#NumPy in-built methods
def q1_b():
    array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])
    array1_flattened=array1.reshape(-1)
    print("Original Array: ", array1)
    print("Flattened Array: ", array1_flattened)


#(c) Compare the following numpy arrays:
#arr1 = np.array([[1, 2], [3, 4]])
#arr2 = np.array([[1, 2], [3, 4]])
def q1_c():
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[1, 2], [3, 4]])
    flag=False
    for i in np.nditer([arr1,arr2]):
        if (i[0]!=i[1]):
            flag=True
            break
    if flag:
        print("Arrays are not equal")
    else:
        print("Arrays are equal")


# (d) Find the most frequent value and their indice(s) in the following arrays:
# i.  x = np.array([1,2,3,4,5,1,2,1,1,1])
# ii.  y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
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


if __name__ == "__main__":
    x = np.array([1,2,3,4,5,1,2,1,1,1])
    y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])

    print("--- Part (a) ---")
    q1_a()

    print("\n--- Part (b) ---")
    q1_b()

    print("\n--- Part (c) ---")
    q1_c()

    print("\n--- Part (d) ---")
    q1_d(x)
    q1_d(y)
    q1_d_loop(x)
    q1_d_loop(y)
# (e) For the array gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]'), find 
# i.  Sum of all elements 
# ii.  Sum of all elements row-wise  
# iii.  Sum of all elements column-wise 
print("---Part (e)---")
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
gfg=np.array(gfg)
print("This is the array matrix :")
print(gfg)
def sum_of_all(gfg):
    sum=0
    for i in gfg.reshape(-1):
        sum+=i

    print("i. Sum of all elements: ", sum)
def sum_row_wise(gfg):
    print("ii. Sum of elements row-wise")
    count=1
    for i in gfg:
        sum=0
    
        for x in i:
            sum+=x
        print(f"Row {count}: {sum}")
        count+=1
def sum_colomn_wise(gfg):
    print("iii. Sum of elements colomn-wise ")
    count=1
    a,b=np.shape(gfg)
    for i in range(0,b):
        sum=0
        for i in gfg[:,i]:
            sum+=i
        print(f"Colomn  {count}: {sum}")
        count+=1
sum_of_all(gfg)
sum_row_wise(gfg)
sum_colomn_wise(gfg)
# Trying to use numpy sum function, learning how axis works.
def sum_axis(gfg):
    gfg1=np.matrix(gfg)
    gfg2= np.array(gfg)
    print(np.sum(gfg1)) #works
    print(np.sum(gfg2)) #works 
    print(np.sum(gfg1,axis=0)) # in case of array it gave a list of sums, cool. In case of matrix it gave a 2-d aray, strange
    print(np.sum(gfg1,axis=1)) # same observation as above, explain this CC
    # observation: matrices are stubborn, they dont change their shape(3,1). 
sum_axis(gfg)
print("---Part (f)---")
# For the matrix: n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]]), find 
# i.  Sum of diagonal elements 
# ii.  Eigen values of matrix 
# iii.  Eigen vectors of matrix 
# iv.  Inverse of matrix 
# v.  Determinant of matrix 
n_array = np.array([[55, 25, 15],[30, 44, 2],[11, 45, 77]])
def Sum_of_Diag_elements(n_array):
    a,b= np.shape(n_array)
    sum_diag=0
    index=0
    for i in n_array:
        if index<b:
            sum_diag+=i[index]
            index+=1
    print(f"i. Sum of Diagnol elements : {sum_diag}")
print("Array: ")
print(n_array)
Sum_of_Diag_elements(n_array)
# SUBMODULE OF LINEAR ALGEBRA UNLOCKED. LINALG pew pew pew
print(f"i. Sum of Diagnol elements: {np.trace(n_array)}")# submodule not used yet
eigVal,eigVec=np.linalg.eig(n_array)
print(f"ii. Eigen values of matrix: {eigVal}")
print(f"iii. Eigen Vectors of matrix: {eigVec}")
print(f"iv. Inverse of matrix: {np.linalg.inv(n_array)}")
print(f"v. Determinant of matrix: {np.linalg.det(n_array)}")
print("---Part (g)---")
# Multiply the following matrices and also find covariance between matrices using NumPy: 
# i.  p = [[1, 2], [2, 3]] 
# q = [[4, 5], [6, 7]] 
# ii.  p = [[1, 2], [2, 3], [4, 5]] 
# q = [[4, 5, 1], [6, 7, 2]]
def multiply_mat(A,B):
    print(f"Array 1: {A}")
    print(f"Array 2: {B}")
    print ("---Multiplication---")
    print(np.dot(A,B))
    print(np.matmul(A,B))
    A=np.array(A)
    B=np.array(B)
    print(A@B)
    print(A*B) # Observation: Wrong answer, gives element wise multiplication 
p = [[1, 2], [2, 3]] 
q = [[4, 5], [6, 7]] 
multiply_mat(p,q)
def covariance(A,B):
    print(np.cov(A,B,rowvar=True))
covariance(p,q)
print("---Part (h)---")
# (h) For the matrices: x = np.array([[2, 3, 4], [3, 2, 9]]); y = np.array([[1, 5, 0], [5, 10, 3]]), 
# find inner, outer and cartesian product?
def Cart(x,y):
    print("Array 1:")
    print(x)
    print("Array 2:")
    print(y)
    print("---Cartesian Product---")
    x=x.reshape(-1)
    y=y.reshape(-1)
    CartProd=[]
    m=len(x)
    n=len(y)
    for i in x:
        for j in y:
            CartProd.append((i,j))
    if (m*n==len(CartProd)):
        CartProd=np.array(CartProd)
        print(CartProd)
    else: print("Error")
def inner_outer(x,y):
    print("---Inner Product---")
    print(np.inner(x,y))
    print("---Outer product---")
    print(np.outer(x,y))
x = np.array([[2, 3, 4], [3, 2, 9]])
y = np.array([[1, 5, 0], [5, 10, 3]])
Cart(x,y)
inner_outer(x,y)