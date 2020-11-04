import sys
from typing import List


# 暴力解决办法：使用滑动窗口办法进行解决
def maxSubArray(nums: List[int]) -> int:
    max_sum = -sys.maxsize
    n = len(nums)
    # 表示设置第一个指针，代表从左向右去判断
    for i in range(n):
        inner_sum = 0
        # 表示设置第二个指针，代表从当前位置到末位判断
        for j in range(i, n):
            inner_sum += nums[j]
            max_sum = max(max_sum, inner_sum)
    return max_sum
