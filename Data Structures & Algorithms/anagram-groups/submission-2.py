class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}
        for each in strs:
            sorted_each = "".join(sorted(each))
            if sorted_each in mapping:
                mapping[sorted_each].append(each)
            else:
                mapping[sorted_each] = [each]

        values = list(mapping.values())
        return values     