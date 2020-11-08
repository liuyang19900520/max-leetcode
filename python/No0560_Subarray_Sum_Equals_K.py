import sys
from typing import List


# 暴力解决办法：使用滑动窗口办法进行解决
def subarraySum(nums: List[int], k: int) -> int:
    n = len(nums)
    total = 0;
    # 表示设置第一个指针，代表从左向右去判断
    for i in range(n):
        inner_sum = 0
        # 表示设置第二个指针，代表从当前位置到末位判断
        for j in range(i, n):
            inner_sum += nums[j]
            if inner_sum == k:
                total = total + 1;
    return total;


# 采用hashmap存储
def subarraySum2(nums: List[int], k: int) -> int:
    hashmap = {}
    acc = count = 0
    for num in nums:
        # acc我们可以代表相加的和
        acc += num
        # 这部分很好理解，就是我们得到目标值k的话，返回值count+1
        if acc == k:
            count += 1
        # acc-k代表了当前位置数组的和-目标值，
        # 如果这个acc-k在hashmap中，也就是可以理解为acc-hashmap中的一个值=k，而我们知道hashmap的值就是之前num到当前位置的和
        # 比如[1,2,3,1] k=6 当num循环到最后一个1的时候，我们的acc-k则等于1 在我们的hashmap中也整好有一个1，这就是说明，从hashmap等于1的那个num之后，到当前的num和为k
        # 同理，比如[1,2,3,3] k=6，当num循环到最后一个3的时候，我们的acc-k等于3，二在我们的hashmap中也有一个3，这说明，从hashmap等于3的那个num之后，到当前的num和为k
        if acc - k in hashmap:
            count += hashmap[acc - k]
        # 我们需要判断目前增加的值是否在map中，如果在就要给map中key为当前和的value +1
        if acc in hashmap:
            hashmap[acc] += 1
        else:
            hashmap[acc] = 1
    return count
