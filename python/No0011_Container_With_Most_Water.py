# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
#  the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x
# -axis forms a container, such that the container contains the most water.
#
#  Notice that you may not slant the container.
#
#
#  Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can conta
# in is 49.
#
#
#  Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
#  Example 3:
#
#
# Input: height = [4,3,2,1,4]
# Output: 16
#
#
#  Example 4:
#
#
# Input: height = [1,2,1]
# Output: 2
#
#
#
#  Constraints:
#
#
#  n = height.length
#  2 <= n <= 3 * 104
#  0 <= height[i] <= 3 * 104
#
#  Related Topics Array Two Pointers
#  👍 7886 👎 646


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution0011:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        area = 0
        # 指定到i<j，也就是双指针需要从左右两边分别获取，不能穿过中线
        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            # 如果左指针比右指针低，就要移动左指针
            # 原因说明，左边低的时候，移动一个左边，如果新的更高，就可能使面积更大
            if height[i] <= height[j]:
                i += 1
            else:
                # 如果左指针比右指针高，就要移动右指针，如果移动后的更高，就可能使面积更大
                j -= 1

        return area

# leetcode submit region end(Prohibit modification and deletion)
