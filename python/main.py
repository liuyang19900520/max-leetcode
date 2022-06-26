from No0144_Tree_Preorder_Traversal import TreeNode
from No0144_Tree_Preorder_Traversal import Solution

# Press the green button in the gutter to run the script.
s = Solution()

root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
result = s.preorderTraversal(root)
print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
