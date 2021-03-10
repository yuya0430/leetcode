# Definition for singly-linked list.
class ListNode:
    def __init__(self, nums):
        self.val = nums[0]
        self.next = self.Gen_next(nums)

    def Gen_next(self, nums):
        if len(nums) == 1:
            return None
        else:
            return ListNode(nums[1:])

#Runtime: 36 ms, faster than 52.17% of Python3 online submissions for Remove Nth Node From End of List.
#Memory Usage: 14.4 MB, less than 18.54% of Python3 online submissions for Remove Nth Node From End of List.
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :type head: ListNode \\
        :type n: integer \\
        :rtype: ListNode
        """

        def getList(head):
            l = []
            while head != None:
                l.append(head)
                head = head.next
            
            return l

        listnode_list = getList(head)
        if len(listnode_list) == 1 and n == 1:
            return None
        elif len(listnode_list)-n == 0:
            return listnode_list[1]
        else:
            head1 = listnode_list[len(listnode_list)-n-1]
            head1.next = listnode_list[len(listnode_list)-n].next

        return head

def main():
    nums = [1,2]
    head = ListNode(nums)
    tmp = head
    n = 2
    sol = Solution()
    tmp = sol.removeNthFromEnd(head, n)
    if tmp != None:
        for i in range(len(nums)-1):
            print(tmp.val)
            tmp = tmp.next
    else:
        print(tmp)
        
if __name__ == "__main__":
    main()