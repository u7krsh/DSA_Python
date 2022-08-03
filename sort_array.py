"""
912. Sort an Array
------------------------------------------------------------------
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


def sortArray(arr,l,r):
    left = l
    right = r

    if left < right:
        mid = left + (right - left) // 2
        # Creating tw subarray
        leftarray = arr[:mid]
        rightarray = arr[mid:]
        sortArray(leftarray, 0, mid)
        sortArray(rightarray, mid+1, len(arr) - 1)

        i,j,k = 0,0,0
        while i < len(leftarray) and j < len(rightarray):
            #print(i,leftarray, j ,rightarray)
            if leftarray[i] > rightarray[j]:
                arr[k] = rightarray[j]
                j +=1
            else:
                arr[k] = leftarray[i]
                i += 1

            k += 1
            # Filling remaining vals form Left arr
        while i < len(leftarray):
            arr[k] = leftarray[i]
            i += 1
            k += 1
        # Filling remaining vals form Right arr
        while j < len(rightarray):
            arr[k] = rightarray[j]
            j += 1
            k += 1
        return arr

array = [5,1,1,2,0,0]
size = len(array)
print(f'Original array -> {array}')
res = sortArray(array,0, size - 1)
print(f'Sorted array -> {res}')