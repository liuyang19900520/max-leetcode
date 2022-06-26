# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
#
#
#  Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#
#
#  Example 2:
#
#
# Input: root = []
# Output: []
#
#
#  Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the tree is in the range [0, 100].
#  -100 <= Node.val <= 100
#
#
#
#  Follow up: Recursive solution is trivial, could you do it iteratively?
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 4319 👎 134


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    p = []
    self.trav(root, p)
    return p

  def trav(self, root, p) -> List[int]:
    if (root == None):
      return p
    p.append(root.val)
    p = self.trav(root.left, p)
    return self.trav(root.right, p)
# leetcode submit region end(Prohibit modification and deletion)
