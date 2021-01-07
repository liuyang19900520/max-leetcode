# Given an array nums of n integers, are there elements a, b, c in nums such tha
# t a + b + c = 0? Find all unique triplets in the array which gives the sum of ze
# ro.
#
#  Notice that the solution set must not contain duplicate triplets.
#
#
#  Example 1:
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2:
#  Input: nums = []
# Output: []
#  Example 3:
#  Input: nums = [0]
# Output: []
#
#
#  Constraints:
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics Array Two Pointers
#  👍 9007 👎 949


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums排序
        nums.sort()
        # 最左侧为k，i和j左右夹逼
        length = len(nums)
        k = 0

        res = []
        # 遍历k，也就是最左侧的参考值
        for k in range(length - 2):
            # 排序后，最左侧如果大于0，则不可能出现三数和=0
            if nums[k] > 0:
                break
            # 如果nums[k]（用作比较的参数，作为另两个数的和的存在的元素重复了，则全跳过，直接对比下一个不同的nums[k]）
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = 1 + k
            j = len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                # nums[k]是参考值，nums[i]最小值，nums[j]最大值，所以要移动i,让小的数字变大
                if s < 0:
                    i += 1
                    # nums[i]也要跳过重复的项目
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                # nums[k]是参考值，nums[i]最小值，nums[j]最大值，所以要移动j，让打的数字变小
                elif s > 0:
                    j -= 1
                    # nums[j]也要跳过重复的项目
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
