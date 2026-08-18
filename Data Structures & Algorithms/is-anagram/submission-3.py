class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        olde = defaultdict(int)
        for char in s:
            olde[char] += 1
        for char in t:
            olde[char] -= 1
        
        res = {char: count for char, count in olde.items() if count != 0}

        print(res)
        
        return len(res.keys()) == 0


        