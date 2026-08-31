from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # match and count matter; position semi matters
        # a hash with occurrences is key
        # w o(1) space relies on constraint of lowercase letters: O(26)

        hash_of_s1 = Counter(s1)

        start, end = 0, 1
        hash_of_window = defaultdict(int)
        hash_of_window[s2[start]] += 1
        len_window = 1

        while start <= len(s2) - len(s1): 

            if len_window == len(s1) or end == len(s2):     
                if hash_of_window == hash_of_s1:
                    return True
                elif start == len(s2) - 1:
                    return False
                else:
                    start += 1
                    hash_of_window = defaultdict(int)
                    hash_of_window[s2[start]] += 1
                    end = start + 1
                    len_window = 1
            else:
                hash_of_window[s2[end]] += 1
                end += 1
                len_window += 1

        return False


        # Wrong problem solved: exact match NOT permuation
        # # position and match matter
        # # possible_starts = {} # char: idx in s1

        # j = 0 # s1
        # running_match = False
        # running_len = 1

        # for i, char in enumerate(s2):
        #     if running_len == len(s1):
        #         if running_match:
        #             return True
        #         else: 
        #             j = 0
        #             running_len = 0

        #     match = s1[j]
        #     if char == match:
        #         running_match = True
        #         running_len += 1                    
        #         j += 1
        #     else:
        #         running_match = False
        #         j = 0
        #         running_len = 0
        # return False
        