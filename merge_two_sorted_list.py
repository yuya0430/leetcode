# Runtime: 40 ms, faster than 49.45% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.1 MB, less than 86.76% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def __init__(self, l1:list, l2:list):
        self.l1 = self.generate(l1)
        self.l2 = self.generate(l2)

    def generate(self, li:list):
        if len(li) == 0:
            return None

        return ListNode(li[0], self.generate(li[1:]))

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        tmp_l1 = l1
        while tmp_l1 != None:
            l1_list.append(tmp_l1.val)
            tmp_l1 = tmp_l1.next

        l2_list = []
        tmp_l2 = l2
        while tmp_l2 != None:
            l2_list.append(tmp_l2.val)
            tmp_l2 = tmp_l2.next

        merge_list = l1_list + l2_list
        merge_list.sort()

        return self.generate(merge_list)

def main():
    sol = Solution([1,2,4], [1,3,4])

    l1 = sol.l1
    l2 = sol.l2

    merge_list = sol.mergeTwoLists(l1, l2)

    tmp = merge_list
    while tmp != None:
        print(tmp.val)
        tmp = tmp.next


if __name__ == "__main__":
    main()