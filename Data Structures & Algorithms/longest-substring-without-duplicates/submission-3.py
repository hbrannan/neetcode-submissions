class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r = 0, 1
        seen = {s[l]: l} 
        max_length = 1 

        while r < len(s):
            char = s[r] 
            # if you hit a dupe, shift positions not len
            if char in seen and seen[char] >= l: # abcdd | abcdar | tmmzuxt | abcabcbb
                last_idx = seen[char]
                l = last_idx + 1 

            this_length = r - l + 1 
            max_length = max(this_length, max_length)
            seen[char] = r
            r += 1

        return max_length

        