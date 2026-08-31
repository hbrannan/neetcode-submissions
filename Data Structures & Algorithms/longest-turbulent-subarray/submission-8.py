class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # We know we can use a sliding window because
        # adjacency matters
        # efficienctly pattern matching a criteria throughout array
        # overlap in the pattern
        # arr=[9,4,2,10,7,8,8,1,9]
        # arr=[4,8,12,16]
        if len(arr) < 2:
            return len(arr)
    
        max_size = 0
        l,r = 0, 1
        last = None

        while r < len(arr): 
            current_el = arr[r-1]
            next_el = arr[r]
            are_same = current_el == next_el 

            if are_same:
                l = r # constitutes break
                last = None # No size update
                max_size = max(max_size, 1)
            elif last is None or (next_el < current_el) != last:
                last = next_el < current_el
                max_size = max(max_size, r-l+1)
            else:
                l = r - 1
                last = next_el < current_el

            r += 1 
        return max_size
        