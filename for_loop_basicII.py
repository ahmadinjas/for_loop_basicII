
#  1 

def biggie_size(arr):
    for i in range (len(arr)):
     if arr[i] > 0 :
        arr [i]= 'big'
    return arr

print(biggie_size([-11,5,5,-9]))

#   2 


def z(count_P): 
   count = 0 
   for i in range(len(count_P)): 
      if count_P[i] > 0 :
          count = count + 1 
    
   count_P [len(count_P)-1] = count

   return count_P


print(z([-1,1,1,1]))
print(z([1,6,-4,-7,-2]))

#   3 

def sum_total(arr):
   count_sum=0 
   for i in range(len(arr)):
      
    count_sum = count_sum + arr[i]
   return count_sum

print(sum_total([1,2,3,4]))


#   4  

def average(arr1):
   average_sum = 0 
   for i in range(len(arr1)): 
    average_sum = average_sum + arr1[i]
   average_sum=average_sum / len(arr1)

   return average_sum

print(average([1,2,3,4]))

#   5 

def length(arr2): 
   length_sum=0 
   for i in range(len(arr2)):
      length_sum = len(arr2)

   return length_sum

print(length([]))
print(length([37,2,1,-9]))

#   6

def minimum(arr):
      if len(arr)==0:
         return False
      min_val = arr[0]
      for i in range(len(arr)):
            if arr[i]<min_val: 
             min_val=arr[i]
      return min_val
print(minimum([]))
print(minimum([37,2,1,-9]))


#   7 

def maximum(arr):
      if len(arr)==0:
         return False
      max_val = arr[0]
      for i in range(len(arr)):
            if arr[i]>max_val: 
             max_val=arr[i]
      return max_val

print(maximum([37,2,1,-9]))
print(maximum([]))

#   8 

def ultimate_analysis(arr):
    if len(arr) == 0:
        return {'sumTotal': 0, 'average': 0, 'minimum': False, 'maximum': False, 'length': 0}
    sumTotal = 0
    min_val = arr[0]
    max_val = arr[0]

    # for i in range(len(arr)):
    #     sumTotal = sumTotal + arr[i]
        
    #     if arr[i] < min_val:
    #         min_val = arr[i]
            
    #     if arr[i] > max_val:
    #         max_val = arr[i]

    # length = len(arr) 
    # average = sumTotal / length

    # return {
    #     'sumTotal': sumTotal,
    #     'average': average,
    #     'minimum': min_val,
    #     'maximum': max_val,
    #     'length': length
    # }
   
print(ultimate_analysis([37,2,1,-9]))
print(ultimate_analysis([]))


#   9 

def reverse_array(arr):
    new_arr = []
    for i in range(len(arr)-1, -1, -1): 
        new_arr.append(arr[i])
    return new_arr

print(reverse_array([37,2,1,-9]))

def ultimate_analysis2(arr):
   if len(arr) == 0 : 
      return {'sumTotal': 0, 'average': 0, 'minimum': False, 'maximum': False, 'length': 0}
   return {
    'sumTotal': sum_total(arr),
    'average': average(arr),
    'minimum': minimum(arr),
    'maximum': maximum(arr),
    'length': length(arr)
   }

print(ultimate_analysis2([20,-2,5]))
print 

