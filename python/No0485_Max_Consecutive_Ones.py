# Given a binary array nums, return the maximum number of consecutive 1's in
# the array.
#
#
#  Example 1:
#
#
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#  The maximum number of consecutive 1s is 3.
#
#
#  Example 2:
#
#
# Input: nums = [1,0,1,1,0,1]
# Output: 2
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 10⁵
#  nums[i] is either 0 or 1.
#
#  Related Topics Array 👍 2571 👎 396

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
      return 0
    count = 0
    result = 0
    for num in nums:
      if nums == 1:
        count = count + 1
      else:
        result = max(result, count)
        count = 0

    return max(result, count)

# leetcode submit region end(Prohibit modification and deletion)
