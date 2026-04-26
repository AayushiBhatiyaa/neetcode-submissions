class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        frq_dict = {i:[] for i in set_nums}
        for i in set_nums:
            frq_dict[i]= nums.count(i)
        # sort the dict with values descending order
        sorted_frq = dict(sorted(frq_dict.items(), 
        key=lambda item: item[1], reverse=True))
        keys_list = list(sorted_frq.keys())
        return keys_list[:k]
