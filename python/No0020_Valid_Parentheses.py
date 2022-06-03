# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid.
#
#  An input string is valid if:
#
#
#  Open brackets must be closed by the same type of brackets.
#  Open brackets must be closed in the correct order.
#
#
#
#  Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
#  Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
#  Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 10⁴
#  s consists of parentheses only '()[]{}'.
#
#  Related Topics String Stack 👍 13337 👎 596


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def isValid(self, s: str) -> bool:
    if len(s) == 0:
      return True
    stack = []
    for c in s:
      if c == '(' or c == '[' or c == '{':
        stack.append(c)
      else:
        if len(stack) == 0:
          return False
        else:
          temp = stack.pop()
          if temp == '(':
            if c != ')':
              return False
          elif temp == '[':
            if c != ']':
              return False
          elif temp == '{':
            if c != '}':
              return False
    if len(stack) == 0:
      return True
    else:
      return False

# leetcode submit region end(Prohibit modification and deletion)
