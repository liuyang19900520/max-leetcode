from No0094_Binary_Tree_Inorder_Traversal import TreeNode
from No0094_Binary_Tree_Inorder_Traversal import Solution

# Press the green button in the gutter to run the script.
s = Solution()

root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
result = s.inorderTraversal(root)
print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
