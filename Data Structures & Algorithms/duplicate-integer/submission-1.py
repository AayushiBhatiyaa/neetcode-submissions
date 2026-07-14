class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        val_key =  set(nums)
        if len(val_key) != len(nums):
            return True
        else:
            return False