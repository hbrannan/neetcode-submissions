from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashed_anagrams = defaultdict(list)
        # (len, sorted): []

        for string in strs:
            key = (len(string), "".join(sorted(string)))
            hashed_anagrams[key].append(string)
        
        for key, anagram_list in hashed_anagrams.items():
            res.append(anagram_list)

        return res
        