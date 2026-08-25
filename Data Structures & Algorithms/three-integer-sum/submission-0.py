class Solution:
    # on^2; O(1) space
    # Because you do not know ultimate sum, you are going to have to search 2 linear spaces
    # Take this as the twoSum problem within a problem, making -i the target sum

    # nums=[-1,0,1,2,-1,-4]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        length = len(nums) # 6
        nums.sort() # [-4,-1,0,1,2]
        seen = set() 
        
        for i in range(length):
            complement_for_pair = -1 * nums[i] # 1
            j = i + 1
            k = length - 1

            while j < k:              
                if nums[j] + nums[k] == complement_for_pair:
                    # j = 2; k = 5; -1 + 2 = 1;; 
                    # -1, -1, 2;; 
                    solve = [nums[i], nums[j], nums[k]] # N.b. - inherently sorted
                    solve_tuple = (solve[0], solve[1])
                    if solve_tuple not in seen:
                        seen.add(solve_tuple)
                        triplets.append(solve) 
                    k -= 1
                
                elif nums[j] + nums[k] < complement_for_pair:
                    j += 1
                    # this one; 2
                else:
                    # > 
                    k -= 1          

        return triplets


        # What if j = length but k not yet = 0; search space done? 
        