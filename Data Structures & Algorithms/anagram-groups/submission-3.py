class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            letter_count = {}
            for letter in string:
                letter_count[letter] = letter_count.get(letter, 0) + 1
            custom_string = ", ".join(f"{k}:{v}" for k, v in sorted(letter_count.items()))
            if custom_string in anagrams:
                anagrams[custom_string].append(string)
            else:
                anagrams[custom_string] = [string]
        result = []
        for _, v in anagrams.items():
            result.append(v)
        return result
