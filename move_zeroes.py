'''
283. Move Zeroes
-----------------------------------------------------------------------------------------------------------------------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

def moveZeroes(nums):

    pos = 0
    for idx in range(len(nums)):

        if nums[idx] != 0:
            nums[pos], nums[idx] = nums[idx], nums[pos]
            pos += 1
    return nums

print(moveZeroes([0,1,0]))