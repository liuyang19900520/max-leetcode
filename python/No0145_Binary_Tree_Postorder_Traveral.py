# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
#
#
#  Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
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
#  The number of the nodes in the tree is in the range [0, 100].
#  -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
# Related Topics Stack Tree Depth-First Search Binary Tree 👍 4477 👎 143


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if root == None:
      return []
    recursive,result =[],[]
    recursive.append(root)
    while recursive:
      current = recursive.pop();
      result.append(current.val)
      if current.left:
        recursive.append(current.left)
      if current.right:
        recursive.append(current.right)

    #倒序输出
    return result[::-1]


# leetcode submit region end(Prohibit modification and deletion)
