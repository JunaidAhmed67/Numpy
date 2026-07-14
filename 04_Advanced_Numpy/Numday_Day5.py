import numpy as np

# arr =np.array([10,20,30,40,50,60])
# arr =np.array([10,20,30,40,50,60])
# new_arr = np.insert(arr,2,1000)
# print(new_arr)
# new_arr = np.insert(arr,2,25)
# print(new_arr)

# arr_2d = np.array([[2,3],[3,4],[5,6]])
# arr = np.insert(arr_2d,1,[1000])
# arr = np.insert(arr_2d,2,[200,300])
# arr = np.insert(arr_2d,2,[200,300],axis=0)
# print(arr)
#-->  APPEND
# arr = np.array([10,20,30])
# new_arr = np.append(arr ,[40,50,60])
# print(new_arr)

# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# new_array = np.concatenate((arr1,arr2))
# print(new_array)


# arr =np.array([10,20,30,40,50,60])
# new_arr = np.delete(arr,2)
# print(arr)
# print(new_arr)


# arr1 = np.array([[10,20,30],[40,50,60]])
# new_array = np.delete(arr1,0,axis=0)
# print(new_array)




# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# new_array = np.vstack((arr1,arr2))
# print(new_array)

# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# new_array = np.hstack((arr1,arr2))
# print(new_array)

import numpy as np

arr = np.array([
    [1, 2, 3, 4, 52,22],
    [12, 13, 14, 15, 16,33]
])

new_array = np.hsplit(arr, 3)   


print(new_array)