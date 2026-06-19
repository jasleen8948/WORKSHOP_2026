# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         nums=nums.sort()
#         return nums

# sort colors
def sortColors(nums):
    nums.sort()
    return nums
nums = [2, 0, 2, 1, 1, 0]
print(sortColors(nums))