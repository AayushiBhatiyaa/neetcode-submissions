class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorts = sorted(s)
        sortt = sorted(t)

        if sorts == sortt:
            return True
        else:
            return False