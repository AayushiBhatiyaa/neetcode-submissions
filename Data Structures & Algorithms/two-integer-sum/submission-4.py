class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_dict = {}

        for i , n in enumerate(nums):
            req = target - n
            if req in previous_dict:
                return [previous_dict[req],i]
            previous_dict[n] = i
