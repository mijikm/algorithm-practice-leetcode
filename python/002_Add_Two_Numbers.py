# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Approach: Elementary Math

# Time Complexity: O(max(m,n))
# assume that m and n represents the length of l1 and l2 respectively
# this algorithm iterates at most max(m,n) times

# Space Complexity: O(max(m,n))
# the length of the new list is at most max(m,n) + 1

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # create dummy head
        dummyHead = ListNode(0)
        p = l1
        q = l2
        # initialise current node to dummy head of the returning list
        current = dummyHead
        # initialise carry to 0
        carry = 0
        # loop through lists l1 and l2 till reaching both ends
        while p is not None or q is not None:
            # set x to node p's value
            x = p.val if p is not None else 0
            # set y to node q's value
            y = q.val if q is not None else 0
            sum = carry + x + y
            # update carry
            carry = sum // 10
            # create a new node with the digit value of (sum mod 10)
            # set it to current node's next
            current.next = ListNode(sum % 10)
            # advance current node to next
            current = current.next
            # advance both p and q
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        # check if carry = 1, if so append a new node with digit 1 to the returning list
        if carry > 0:
            current.next = ListNode(carry)
        # return dummy head's next node
        return dummyHead.next
