class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        area = 0
        # I need to find a minimum left bound and a minimum right bound; else return 0
        # Once i know this, I can begin to trust water accumulation

        # In order to deal with the time and memory constraints, I need to act on inferences from inequalities instead of certainties
        # Which side is greater or lesser will be *VERY* important

        l, r = 0, len(height) - 1
        left_wall = height[l] # initiate them at essentially Null value
        right_wall = height[r]

        while l < r:
            if left_wall < right_wall:
                # Left is the constraint because *at some point* right wall will "trap" the water even if not immediately
                # So, I can (for now) freely focus on calculating "current" relative only to left.

                l += 1 # Move left to differentiate it from the l_max it just was
                left_wall = max(left_wall, height[l]) # Update if I am at a new max
                area += left_wall - height[l] # This will never be 0 bc just made  max 1st operator in this expression
            else:
                # if equal, it doesn't matter which side advances; if greater, right (lesser) *must* advance
                r -= 1
                right_wall = max(right_wall, height[r])
                area += right_wall - height[r] # again, always positive or 0; never negative

        return area



        # height=[0,1,0,2,1,0,1,3,2,1,2,1]
        # total_units = 0 # 

        # left, current, right = 0, 1, 2 # 
        # left_h = height[left] # Hold outside of idx progression
        # local_units = 0 

        # while right < len(height): # 
        #     right_h = height[right] # 

        #     if not left_h: # Y;1->N; 
        #         left, current, right = left + 1, current + 1, right + 1 
        #         left_h = height[left]
        #         continue

        #     current_h = height[current] # 0
        #     if current_h < left_h:
        #         local_units += left_h - current_h # 1-0(1);
            
        #     print('right_h', right_h, 'left_h', left_h, 'loc_vol', local_units, '->', total_units)

        #     if right_h >= left_h: # 
        #         # Have reached a max fill line; add then reset local count & move:
        #         total_units += local_units # 0+1(1)
        #         local_units = 0

        #         left, current, right = right, right + 1, right + 2 # 2/3/4
        #         left_h = height[left] # 
        #     else:
        #         # OK if no pockets lower than last "L", but there could be; so need a mechanism to reset a smaller relative L
        #         # Track local value and keep it moving
        #         left, current, right = left + 1, current + 1, right + 1 #  
        