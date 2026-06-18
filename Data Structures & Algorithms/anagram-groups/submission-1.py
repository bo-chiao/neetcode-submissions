class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        result_dict = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = len(anagram_dict)
            result_dict.append((word, anagram_dict[sorted_word]))
        result = [[] for _ in range(len(anagram_dict))]
        for word, group in result_dict:
            result[group].append(word)
        return result
