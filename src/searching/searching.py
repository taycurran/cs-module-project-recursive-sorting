# TO-DO: Implement a recursive implementation of binary search
arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
arr2 = []

# def binary_search(arr, target, start, end):
#     # find mid
#     start_i = 0
#     mid_i = len(arr) // 2
#     mid_e = arr[mid_i]
#     end_i = -1

#     if mid_e == target:
#         return mid_i
#     elif mid_e > target:
#         start_i = start_i
#         end_i = mid_i
#         new_arr = arr[start_i: end_i]
#         new_mid_i = len(new_arr) // 2
#         binary_search(new_arr, target, start_i, end_i)
#     elif mid_e < target:
#         start_i = mid_i + 1
#         end_i = end_i
#         new_arr = arr[start_i: end_i]
#         if len(new_arr) == 0:
            
#         else:
#             new_mid_i = len(new_arr) // 2
#             binary_search(new_arr, target, start_i, end_i)4 //

# 

def binary_search(arr, target, start=0, end=None):
    if end >= start:
        mid = (end + start) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1
    




    
    # compare to target
    # find new mid


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass


# binary_search(arr1, -8, 0, len(arr1)-1)
