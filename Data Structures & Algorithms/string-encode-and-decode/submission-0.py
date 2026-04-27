class Solution:

    def encode(self, strs: List[str]) -> str:
        # add string length to start and # for the append of next string
        new_str_list = []
        for each in strs:
            count = str(len(each))
            new_str_list.append(f"{count}#{each}")
        
        return "".join(new_str_list)

    def decode(self, s: str) -> List[str]:
        # split the string
        i = 0
        decoded_list = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            start = j+1
            end = start + length
            part = s[start:end]
            decoded_list.append(part)
            i = end
            
        return decoded_list
