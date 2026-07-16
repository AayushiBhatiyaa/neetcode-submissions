class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiply_list = []
        for index, num in enumerate(nums):
            multi = 1
            for j in range(index+1,len(nums)):
                multi *= nums[j]
            if index !=0:
                for j in range(0,index):
                    multi *= nums[j]
            multiply_list.append(multi)

        return multiply_list