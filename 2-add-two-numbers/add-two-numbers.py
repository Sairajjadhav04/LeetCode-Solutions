class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = ""
        num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        total = int(num1) + int(num2)
        result = str(total)[::-1]
        dummy = ListNode(0)
        current = dummy
        for digit in result:
            current.next = ListNode(int(digit))
            current = current.next
        return dummy.next