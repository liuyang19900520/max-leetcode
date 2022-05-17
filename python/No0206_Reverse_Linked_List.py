# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
#  Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
#
#
#  Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is the range [0, 5000].
#  -5000 <= Node.val <= 5000
#
#
#
#  Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#  Related Topics Linked List Recursion 👍 11865 👎 206


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head

    while head is not None and head.next is not None:
      # 将位于列表首位的dummy的next取出来
      dnext = dummy.next
      # 将位于循环中的head的next取出来
      hnext = head.next

      # 交换开始
      # 首位换位置
      dummy.next = hnext
      # 循环中的位置替换成下一个
      head.next = hnext.next
      # 原来下一个的位置，替换为dummy.next，也就是当前循环cur
      hnext.next = dnext
    return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
