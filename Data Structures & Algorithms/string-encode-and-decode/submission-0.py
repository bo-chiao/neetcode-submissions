class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        result = []
        while j < len(s):
            if s[j] == '#':
                s_length = int(s[i:j])
                i = j + 1
                j += (s_length + 1)
                result.append(s[i:j])
                i = j 
            j += 1
        return result

            
                
            
