# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # ith node of LL is the twin of the n-1-ith node
        # twin sum == sum of node + twin

        # find the middle w/ iteration 1, can assume IS EVEN
        # a move in counter-LL dir adds o(n) ea time
        # should i hash these? 
        # trick: you can reverse 1/2 of the LL to get your pairs to work without needing to reverse dirs

        # find the mid, leave 2nd pointer here
        # reverse the 1st half until hit mid
        # reset 1st pointer to head

        # head.next + mid.next; check if gt max; 
        # cte til mid = None

        front, back = head, head

        prev = None

        while front and front.next:
            front = front.next.next 
            towards_middle = back.next # ends at midpoint
            back.next = prev # in place, reverses the list
            prev = back
            back = towards_middle

        # Reset
        res = 0
        while back:
            res = max(res, prev.val + back.val)
            prev = prev.next
            back = back.next

        return res



        
        