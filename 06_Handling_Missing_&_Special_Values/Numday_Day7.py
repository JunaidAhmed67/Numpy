import numpy as np


# arr = np.array([1,np.nan,3,4,np.nan,6])
# print(np.isnan(arr))
# print(np.nan_to_num(arr))
# print(np.nan_to_num(arr,nan=11))

# arr = np.array([1,np.inf,3,4,-np.inf,6])
# cleaned_data = np.nan_to_num(arr, posinf=1000,neginf=-1000)
# print(np.isposinf(arr))


#practice questions
#Q1 Check which values are NaN.
# arr = np.array([10, np.nan, 30, np.nan, 50])
# arr = np.isnan(arr)
# print(arr)

#Q2 Count how many NaN values are present.
# arr = np.array([10, np.nan, 30, np.nan, 50])
# arr = np.sum(np.isnan(arr))
# print(arr)

#Q3 Print only the NaN values.
# arr = np.array([1, np.nan, 3, np.nan, 5])
# # arr = [np.isnan(arr)]
# print(arr[np.isnan(arr)])


#Q4 Print only the non-NaN values.
# arr = np.array([1, np.nan, 3, np.nan, 5])
# arr = arr[~np.isnan(arr)]
# print(arr)

#Q5 Replace all NaN values with 0.
# arr = np.array([10, np.nan, 30])
# arr = np.nan_to_num(arr)
# print(arr)

#Q6 Replace NaN with 100.
# arr = np.array([10, np.nan, 30])
# arr = np.nan_to_num(arr,nan=100)
# print(arr)

#Q7 Replace NaN with -1.
# arr = np.array([10, np.nan, 30])
# arr = np.nan_to_num(arr,nan=-1)
# print(arr)

#Q8 Replace all NaN values with 999.
# arr = np.array([10, np.nan, 30])
# arr = np.nan_to_num(arr,nan=999)
# print(arr)

#Q9 Find infinite values.
# arr = np.array([10, np.inf, 30, -np.inf, 50])
# arr = arr[np.isinf(arr)]
# print(arr)

#Q10 Count infinite values.
arr = np.array([10, np.inf, 30, -np.inf, 50])
arr = np.sum(np.isinf(arr))
print(arr)

