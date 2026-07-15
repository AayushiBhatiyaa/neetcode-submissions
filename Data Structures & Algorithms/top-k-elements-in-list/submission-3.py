class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_order = {}
        setted_list = set(nums)
        for i in setted_list:
            count_num = nums.count(i)
            if count_num in dict_order:
                dict_order[count_num].append(i)
            else:
                dict_order[count_num] = [i]
        
        frq = sorted(list(dict_order.keys()),reverse= True)
        k_req = frq[:k]
        min_heap = []
        for key in k_req:
            min_heap.extend(dict_order[key])
            if len(min_heap) == k:
                break

        return min_heap