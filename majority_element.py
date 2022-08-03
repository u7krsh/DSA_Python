'''
169. Majority Element
----------------------------------------------------------
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
'''

from typing import List

# O(n), O(n) Solution
def majorityElement(nums):
    dic = {}
    max_cnt = 0
    maj_count = len(nums) // 2 + 1
    for val in nums:
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1

    for num in dic:
        cnt = dic[num]
        if cnt >= maj_count:
            max_cnt = num
    return max_cnt


# O(n), O(1) Solution
def majorityElement(nums: List[int]) -> int:

    count = 0
    maj_element = None
    for i in range(len(nums)):
        if count == 0:
            maj_element = nums[i]
        if nums[i] == maj_element:
            count += 1
        else:
            count -= 1
    return maj_element

print(majorityElement([1,3,3,1]))