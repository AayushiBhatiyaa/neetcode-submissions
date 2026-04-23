class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return [0]
        elif len(nums) == 2:
            return [0,1]
        else:
            for index, num in enumerate(nums):
                for i in range(len(nums[index+1:])):
                    next_index = i + index + 1
                    num_2 = nums[next_index]
                    sum_val = num + num_2
                    if sum_val == target:
                        return [index,next_index]