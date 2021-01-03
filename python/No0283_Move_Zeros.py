# Given an array nums, write a function to move all 0's to the end of it while m
# aintaining the relative order of the non-zero elements.
#
#  Example:
#
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
#  Note:
#
#
#  You must do this in-place without making a copy of the array.
#  Minimize the total number of operations.
#  Related Topics Array Two Pointers
#  👍 4710 👎 146


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution0283:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 记录非0元素的位置
        j = 0
        n = len(nums)
        # 循环数组
        for i in range(n):
            # 当数组中的i元素不是0的时候
            if nums[i] != 0:
                # 将这个元素放到j的位置，由于只有当元素i不为0的时候j才+1，所以我们可以理解为，j永远小于等于i
                nums[j] = nums[i]
                # 什么时候会发生j!=i的情况呢，就是已经出现0的情况，
                # 也就是说，在上一个循环中，nums[i-1]等于0，i加了1，j没有+1，
                # 我们就可以将当前的i设置为0，j代表非0数组的位置。
                # 上面虽然做了一个0和非0的位置对调，在下一个循环的时候，i+1，非零位置的j也+1
                if j != i:
                    nums[i] = 0
                j += 1
# leetcode submit region end(Prohibit modification and deletion)
