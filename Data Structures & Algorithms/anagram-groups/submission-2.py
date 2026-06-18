class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def charCount(s: str) -> tuple:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            return tuple(count)
        
        hashmap = {}
        for s in strs:
            key = charCount(s)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return list(hashmap.values())
