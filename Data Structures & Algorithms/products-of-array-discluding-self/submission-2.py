# import math # math.prod(list)
from functools import reduce
    # naive is to get the product of all others ea time O(n^2)
    # opt next is to get the product once then iterate thru 1x dividing by ea el @ el
    # next was pre arr, post arr, store products through 1 pass; take 2nd pass to multiply sol; still O(n^2)

    # [1,2,4,6]

    # Prefix Products
    # [[], [1], [1,2], [1,2,4]]

    # Suffix
    # [[2,4,6], [4,6], [6], []]

    # -> [48, 24, ]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Val * all in Pre * all in Post
        length = len(nums) # 4 
        output = [1] * length
     
        pre_product = 1 
        for i in range(length):
            # @ i, building_product x num; store it @ i of output
            if i > 0:
                num = nums[i - 1]
                pre_product *= num
            output[i] = pre_product
        
        post_product = 1 # 24
        # 1,1,2,8
        # 48,24,6,1
        # 48,24,12,8
        # Expect [48,24,12,8]
        for j in range(length - 1, -1, -1): # 4 -> -1
            if j < length - 1:
                post_num = nums[j+1] 
                post_product *= post_num
            output[j] = output[j] * post_product
        return output
