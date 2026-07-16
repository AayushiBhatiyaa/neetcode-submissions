class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        elif strs == []:
            return "True"
        elif strs:
            # print(strs)
            str_encode = "SPLIT".join(strs)
            print(str_encode)
            return str_encode
        else:
            return ""

    def decode(self, s: str) -> List[str]:
        if s == "True":
            return []
        elif s == "":
            return [""]
        elif s:
            split_str = s.split("SPLIT")
            return split_str
        else:
            return [""]