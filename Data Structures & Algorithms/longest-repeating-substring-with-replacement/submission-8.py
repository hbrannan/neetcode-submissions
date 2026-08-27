class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        seen = defaultdict(int)
        max_len = 0

        max_frequency_ct = 0
        max_char = ""

        while r < len(s):
            substr_len = r - l + 1
            char = s[r]
            # print(f'L:{l}{s[l]}', f'R:{r}{s[r]}', seen, max_frequency_ct, max_char, '->', max_len)

            seen[char] += 1 # 4
            if seen[char] > max_frequency_ct:
                max_frequency_ct = seen[char]
                max_char = char

            if substr_len - max_frequency_ct > k:
                # print('removing', substr_len, max_frequency_ct, k)
                # print()
                remove_char = s[l]
                if remove_char == max_char:
                    max_frequency_ct -= 1
                    max_char = max(seen, key=seen.get) # returns key for max val in dict
                seen[remove_char] -= 1

                l += 1 # Why just 1 to the L always?

            max_len = max(max_len, r - l + 1)
            r += 1

            # s="AAABABB"
            # k=1

        return max_len








        # if len(s) <= k:
        #     return len(s)
        
        # l, r = 0, 1
        # current_letter = s[0]
        # current_k = k 
        # longest_len, this_len = 1, 1

        # while r < len(s): #k = 2 ; AAABBABBAAABABB; BAAA' ABBB
        #     char = s[r] #B
        #     if char == current_letter:
        #         this_len += 1
        #     elif current_k:
        #         this_len += 1
        #         current_k -= 1
        #     else:
        #         # reset l and counts
        #         l = max(r - k, l+1) # 1 
        #         current_letter = s[l] #B
        #         current_k = k
        #         this_len = 1

        #     longest_len = max(this_len, longest_len)
        #     r += 1
            
        # return min(longest_len + current_k, len(s))



        # l = 0
        # count = {}
        # max_freq = 0
        # longest_len = 0

        # for r in range(len(s)):
        #     count[s[r]] = count.get(s[r], 0) + 1
        #     max_freq = max(max_freq, count[s[r]])

        #     if (r - l + 1) - max_freq > k:
        #         count[s[l]] -= 1
        #         l += 1
        