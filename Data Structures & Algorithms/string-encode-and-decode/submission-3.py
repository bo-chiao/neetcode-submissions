class Solution:

    def encode(self, strs: List[str]) -> str:
        output_str = ""
        for string in strs:
            n = len(string)
            output_str += str(n)
            output_str += "#"
            output_str += string
        return output_str

    def decode(self, s: str) -> List[str]:
        output_strs = []
        i = 0
        while i < len(s):
            n_str = ""
            while s[i] != "#":
                n_str += s[i]
                i += 1
            n = int(n_str)
            i += 1
            output_strs.append(s[i:i+n])
            i += n
        return output_strs
