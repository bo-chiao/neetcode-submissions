class Solution:

    def encode(self, strs: List[str]) -> str:
        res_list = []
        for s in strs:
            res_list.append(f"{len(s)}#{s}")
        return "".join(res_list)

    def decode(self, s: str) -> List[str]:
        output_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            n = int(s[i:j])
            i = j + 1
            output_strs.append(s[i:i+n])
            i += n
        return output_strs
