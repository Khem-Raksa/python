# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        cur1 = l1
        cur2 = l2
        temp = ""
        temp2 = ""
        while(cur1):
            temp = temp + (str(cur1.val))
            temp[::-1]
            cur1 = cur1.next
        while(cur2):
            temp2 = temp2 + (str(cur2.val))
            temp = temp2[::-1]
            cur2 = cur2.next
        
        temp = int(temp)
        temp2 = int(temp2)
        print(temp)







a = Solution()
a.addTwoNumbers([2,4,3],[5,6,4])