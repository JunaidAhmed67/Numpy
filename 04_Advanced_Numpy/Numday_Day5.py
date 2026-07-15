import numpy as np

arr =np.array([10,20,30,40,50,60])
arr =np.array([10,20,30,40,50,60])
new_arr = np.insert(arr,2,1000)
print(new_arr)
new_arr = np.insert(arr,2,25)
print(new_arr)

arr_2d = np.array([[2,3],[3,4],[5,6]])
arr = np.insert(arr_2d,1,[1000])
arr = np.insert(arr_2d,2,[200,300])
arr = np.insert(arr_2d,2,[200,300],axis=0)
print(arr)
#-->  APPEND
arr = np.array([10,20,30])
new_arr = np.append(arr ,[40,50,60])
print(new_arr)

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
new_array = np.concatenate((arr1,arr2))
print(new_array)


arr =np.array([10,20,30,40,50,60])
new_arr = np.delete(arr,2)
print(arr)
print(new_arr)


arr1 = np.array([[10,20,30],[40,50,60]])
new_array = np.delete(arr1,0,axis=0)
print(new_array)




arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
new_array = np.vstack((arr1,arr2))
print(new_array)

arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
new_array = np.hstack((arr1,arr2))
print(new_array)


arr = np.array([
    [1, 2, 3, 4, 52,22],
    [12, 13, 14, 15, 16,33]
])

new_array = np.hsplit(arr, 3)   


print(new_array)


#practice questions 
#Q1 Insert 99 at index 2.
arr = np.array([10,20,30,40,50])
arr = np.insert(arr,2,99)
print(arr)


#Q2 Insert 100 at the beginning.
arr = np.array([10,20,30,40,50])
arr = np.insert(arr,0,100)
print(arr)


#Q3 Insert 500 at the end.
arr = np.array([10,20,30,40,50])
arr = np.insert(arr,len(arr),500)
print(arr)


#Q4 Insert -1 before 40.
arr = np.array([10,20,30,40,50])
arr = np.insert(arr,2,-1)
print(arr)


#Q5 Append 60.
arr = np.array([10,20,30,40,50])
arr = np.append(arr,60)
print(arr)


#Q6 Append multiple values 70,80,90.
arr = np.array([10,20,30,40,50])
arr = np.append(arr,[60,70,80,90])
print(arr)



#Q7 Append another array.
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([100,200])
arr = np.append(arr1,arr2)
print(arr)



#Q8 Join these arrays.
a = np.array([1,2,3])
b = np.array([4,5,6])
c=np.concatenate((a,b))
print(c)



#Q9 Concatenate three arrays.
a = np.array([1,2])
b = np.array([3,4])
c = np.array([5,6])
d = np.concatenate((a,b,c))
print(d)



#Q10 Delete the first element.
arr = np.array([10,20,30,40,50])
arr = np.delete(arr,0)
print(arr)



#Q11 Delete 30.
arr = np.array([10,20,30,40,50])
arr = np.delete(arr,2)
print(arr)




#Q12 Delete the last element.
arr = np.array([10,20,30,40,50])
arr = np.delete(arr,-1)
print(arr)




#Q13 Stack vertically.
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))
print(c)




#Q14 Vertically stack three arrays.
a = np.array([1,2])
b = np.array([3,4])
c = np.array([5,6])
d = np.vstack((a,b,c))
print(d)


#Q15 Horizontally stack.
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.hstack((a,b))
print(c)



#Q16 Horizontally stack three arrays.
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.hstack((a,b,np.array([67,56,45])))
print(c)



#Q17 Split the array into 2 equal parts.
arr = np.array([10,20,30,40,50,60])
arr = np.split(arr,2)
print(arr)



#Q18 Split the array into 3 equal parts.
arr = np.array([10,20,30,40,50,60])
arr = np.split(arr,3)
print(arr)



#Q19 Split into 2 parts.
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
arr = np.vsplit(arr,2)
print(arr)




#Q20 Split into 4 parts.
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
arr = np.vsplit(arr,4)
print(arr)



#Q21 Split into 2 parts.
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
arr = np.hsplit(arr,2)
print(arr)




#Q22 Split into 4 parts.
arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
arr = np.hsplit(arr,4)
print(arr)


#Q23 First concatenate them, then append 100.
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b))
c = np.append(c,100)
print(c)



#Q24 Insert 999 at index 1, then delete the last element.
arr = np.array([10,20,30,40])
arr = np.insert(arr,1,999)
arr = np.delete(arr,-1)
print(arr)



#Q25 Create these arrays:
   # Append 70 to a.
   # Insert 99 at index 1 in a.
   # Concatenate a and b.
   # Vertically stack a and b.
   # Horizontally stack a and b.
   # Delete 20 from a.
   # Split [1,2,3,4,5,6] into 3 equal parts.

a = np.array([10,20,30])
b = np.array([40,50,60])

print("Append:", np.append(a,70))

print("Insert:", np.insert(a,1,99))

print("Concatenate:", np.concatenate((a,b)))

print("Vertical Stack:")
print(np.vstack((a,b)))

print("Horizontal Stack:")
print(np.hstack((a,b)))

print("Delete:", np.delete(a,1))

arr = np.array([1,2,3,4,5,6])
print("Split:")
print(np.split(arr,3))