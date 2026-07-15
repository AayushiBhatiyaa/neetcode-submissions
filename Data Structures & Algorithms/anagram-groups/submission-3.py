class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ana = {}

        for each in strs:
            sorted_each = "".join(sorted(each))
            if sorted_each in dict_ana:
                dict_ana[sorted_each].append(each)
            else:
                dict_ana[sorted_each] = [each]

        return_val = list(dict_ana.values())
        return return_val