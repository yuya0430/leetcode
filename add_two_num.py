#計算速度もメモリ使用量もちょうど真ん中くらい

import re

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def generate_next(self, ln1, ln2, carry):
        #---Noneが入力されたときの処理---#
        if ln1 == None:
            ln1 = ListNode(0, None)
        if ln2 == None:
            ln2 = ListNode(0, None)

        #---終了条件：両方とも next が None のとき---#
        if ln1.next == None and ln2.next == None:
            SUM = ln1.val + ln2.val + carry
            if SUM >= 10:
                sum_val = SUM - 10
                carry = 1
                return ListNode(sum_val, ListNode(1))
            else:
                return ListNode(SUM)

        #---再帰処理---#
        else:
            SUM = ln1.val + ln2.val + carry
            if SUM >= 10:
                sum_val = SUM - 10
                carry = 1
            else:
                sum_val = SUM
                carry = 0

            return ListNode(sum_val, self.generate_next(ln1.next, ln2.next, carry))
    
    def addTwoNumbers(self, l1, l2):
        carry = 0
        output = self.generate_next(l1, l2, carry)

        return output

def main():
    list1 = ListNode(2, ListNode(4, ListNode(3)))
    list2 = ListNode(5, ListNode(6, ListNode(4)))

    solution = Solution()
    output = solution.addTwoNumbers(list1, list2)
    

if __name__ == '__main__':
    main()