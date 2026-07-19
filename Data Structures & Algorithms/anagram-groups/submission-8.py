class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            key = [0] * 26
            
            for c in string:
                key[ord(c) - ord("a")] += 1

            anagrams[tuple(key)].append(string)
        
        result = []

        for anagram in anagrams.values():
            result.append(anagram)

        return result
