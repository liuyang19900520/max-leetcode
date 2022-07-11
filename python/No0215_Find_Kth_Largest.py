# Given an integer array nums and an integer k, return the kᵗʰ largest element
# in the array.
#
#  Note that it is the kᵗʰ largest element in the sorted order, not the kᵗʰ
# distinct element.
#
#
#  Example 1:
#  Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#  Example 2:
#  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
#  Constraints:
#
#
#  1 <= k <= nums.length <= 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#
#  Related Topics Array Divide and Conquer Sorting Heap (Priority Queue)
# Quickselect 👍 10760 👎 556


# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    maxHeap = nums
    heapq._heapify_max(maxHeap)
    while k > 0:
      # 每次都pop出最大的
      x = heapq._heappop_max(maxHeap)
      # pop到第k个
      k -= 1
    return x

  # 最小堆的方法。
  def findKthLargest2(self, nums: List[int], k: int) -> int:
    heap = []

    for x in nums:
      if len(heap) < k or x > heap[0]:
        heapq.heappush(heap,x)
      if (len(heap) > k):
        heapq.heappop(heap)
        heapq.heapify(heap)
    return heapq.heappop(heap)

# leetcode submit region end(Prohibit modification and deletion)
