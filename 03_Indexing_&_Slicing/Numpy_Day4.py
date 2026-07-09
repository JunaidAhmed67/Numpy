import numpy as np

# arr =np.array([10,20,30,40,50])
# print(arr[1]) #2nd ele
# print(arr[-1]) #last ele
   
# arr = np.array([10,20,30,40,50,60])
# [atart:stop(ex):step]
# print(arr[1:4]) #4th ind is ex
# print(arr[1::2]) 
# print(arr[::2]) 
# print(arr[:4:]) 
# print(arr[::-1]) #reverse array

# print(arr[[2,4,5]]) #select multiple element at onece
# print(arr[arr>30] ) #select multiple element at onece
# arr = np.array([10,20,30,40,50,60])
# print(arr.reshape(2,3)) # change the actual array
# arr1 = np.array([[10,20,30,],[40,50,60]])
# print(arr1.flatten()) # copy the arry , dont change it
# print(arr1.ravel()) # change the actual array


arr = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
])

# Q1 Print the first element.
# print(arr[0,0])
# Q2 Print 70.
# print(arr[1,2])
# Q3 last number using negative index.
# print(arr[-1,-1])
# Q4 100 number using negative index.
# print(arr[-1,-3])
# Q5 Print the first row.
# print(arr[0])
# Q6 Print the second column.
# print(arr[:,1])
# Q7 Print the last column.
# print(arr[:,-1])
# Q8 Print the first two rows.
# print(arr[:2])
"""Q9 print [[60 70]
             [100 110]]"""
# print(arr[1:3,1:3])
"""Q10 print [[20 30]
             [60 70]]"""
# print(arr[:2,1:3])
"""Q11 print [30 70 110]"""
# print(arr[:,2])

# arr = np.array([10,20,30,40,50,60,70,80])

# # Q13 10 40 80
# print(arr[[0,3,7]])
# # Q14 20 50 70
# print(arr[[1,4,6]])
# # Q15 80 60 20
# print(arr[[7,5,1]])

# arr = np.array([12,25,37,40,52,63,75,88])

# # Q16 Print numbers greater than 50.
# print(arr[arr>50])
# # Q17 Print numbers less than 40.
# print(arr[arr<40])
# # Q18 Print even numbers.
# print(arr[arr%2==0])
# # Q19 Print odd numbers.
# print(arr[arr%2 !=0])
# # Q20 Print numbers between 30 and 70.
# print(arr[(arr>30) & (arr<70)])

# arr = np.arange(1,13)

# # Q21 Convert it into a 3×4 matrix
# print(arr.reshape(3,4))
# # Q22 Convert the same array into 2×6.
# print(arr.reshape(2,6))
# # Q23 Convert the same array into 4x3.
# print(arr.reshape(4,3))


arr = np.array([
    [1,2,3],
    [4,5,6]
])

# Q24 Convert the array into a 1D array using ravel().
print(arr.ravel())
# Q24 Convert the array into a 1D array using flatten().
print(arr.flatten())