class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i,0) + 1

        sorted_counts = sorted(counts.items(), key = lambda x : x[1], reverse= True)
        # print(sorted_counts)

        result = []
        for i in range(k):
            result.append(sorted_counts[i][0])
            
        return result
        # dict_order = {}
        # setted_list = set(nums)
        # for i in setted_list:
        #     count_num = nums.count(i)
        #     if count_num in dict_order:
        #         dict_order[count_num].append(i)
        #     else:
        #         dict_order[count_num] = [i]
        
        # frq = sorted(list(dict_order.keys()),reverse= True)
        # k_req = frq[:k]
        # min_heap = []
        # for key in k_req:
        #     min_heap.extend(dict_order[key])
        #     if len(min_heap) == k:
        #         break

        # return min_heap