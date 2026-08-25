class Solution:
    # on^2; O(1) space
    # Because you do not know ultimate sum, you are going to have to search 2 linear spaces
    # Take this as the twoSum problem within a problem, making -i the target sum

    # nums=[-1,0,1,2,-1,-4]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        length = len(nums) 
        nums.sort() 
        seen = set() 
        
        for i in range(length):
            complement_for_pair = -1 * nums[i] 
            j = i + 1
            k = length - 1

            while j < k:              
                if nums[j] + nums[k] == complement_for_pair:
                    solve = [nums[i], nums[j], nums[k]] # N.b. - inherently sorted
                    solve_tuple = (solve[0], solve[1])
                    if solve_tuple not in seen:
                        seen.add(solve_tuple)
                        triplets.append(solve) 
                    k -= 1
                
                elif nums[j] + nums[k] < complement_for_pair:
                    j += 1
                else:
                    k -= 1          

        return triplets


'''
Discussion post-facto:

First, threeSum is likely twoSum with a little bit more complexity. How to get "target" from threeSum? 
*If* you are willing to use the first element as an anchor, you can say that the other two need to add up to the inverse of that. Otherwise, you will need to use an operation that checks if the three equate to 0. Both are usuable and useful. The former is preferred because this breaks the problem more discreetly into two subproblems. 

Saying that -(l + r) = anchor means that we can now work to get the problem in a shape to solve TwoSum with -(l + r) as the target. 

There are a few additional constraints: O(m) space and On^2 time. In this problem, elements can be reused multiple times for different solution sets but should not be re-used as duplicates. This means: some way of building or tracking comparison is needed *and* min-heap is really not going to be that useful unless you want to rebuild it all the time.  

So first: if we sort the list outside of our loops, this is going to be negligible time complexity addition *and* it seems essential given the complexity constraints. 

Declare our output. We're returning lists of lists, so we'll append each time; no need for a list size. 

Next: 
A. break the problem into an iteration that will use the first idx as an anchor, the inverse of which is the target. 
B. Inside this loop, build something akin to a 2Sum, knowing that the list is sorted. You need a left idx, right idx, and 3 conditions: < target, > target, == target. *Since it is sorted, you will know which whay to move 
- left idx should initialize 1 greater than "anchor"; right @ end
- < target, increase the smaller num by increasing left pointer; leave others the same
- > target, decrease the larger num by decreasing right pointer; leave others the same
- == target: 
    #1 -> First: can't have dupes. 
    - You can either ensure this isn't the case by checking a hash *now* or operationally forbidding in-process. 
    - Having a hash of the output is fine because its O(2m) which is O(m); this will enable simpler code. 
    - The first 2 els will always have the same 3rd; they will always be in stable order
    - I didn't do this, but the published solution suggests:  if you make sure each of your pointers move to a num > (or less as applicable) than their prev, this will also ensure no dupes.
    - If not dupe, append to solution.
    - Next, you need to increment in *only one* direction - can be left or right, but not both. Either will fully cover the problem space. 
C. Stop when l < r to prevent them overlapping for false solutions
D. Return solutions

'''

        