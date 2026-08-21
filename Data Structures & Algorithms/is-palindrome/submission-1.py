import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # find what ceil of "half" is; this is num steps
        # create 2 idx pointers
        # 1 = ciel(half)
        # 2 = floor (half)
        # for ea step
        # is it the same? No -> False
        # pointer 1 increases; pointer 2 decreases
        # if reach the end, True

        # Was it a car or a cat I saw?
        # Strip all spaces*nonalpha-numerics
        # all lower case

        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).casefold()

        half_length = math.ceil(len(cleaned_s) / 2) # 3.5 -> 4
        pre = math.floor(len(cleaned_s) / 2) if len(cleaned_s) % 2 else len(cleaned_s) // 2 - 1 # 3
        post = math.floor(len(cleaned_s) / 2) if len(cleaned_s) % 2 else len(cleaned_s) // 2

        print(range(half_length), pre, post)

        for step in range(half_length):
            if cleaned_s[pre] != cleaned_s[post]: 
                return False
            pre -= 1
            post += 1
        
        return True
