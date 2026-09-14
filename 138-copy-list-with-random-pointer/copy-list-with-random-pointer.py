"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None :
            return None 
        old_new = {}
        current = head 
        while current : 
            old_new[current]=Node(current.val)
            current = current.next 

        current = head
        while current : 
            copy = old_new[current]
            copy.next = old_new.get(current.next)
            copy.random=old_new.get(current.random)
            current = current.next 
        return old_new[head]        