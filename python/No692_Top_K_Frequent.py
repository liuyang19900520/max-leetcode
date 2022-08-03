# Given an array of strings words and an integer k, return the k most frequent
# strings.
#
#  Return the answer sorted by the frequency from highest to lowest. Sort the
# words with the same frequency by their lexicographical order.
#
#
#  Example 1:
#
#
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
#
#
#  Example 2:
#
#
# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"],
#  k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
#  Constraints:
#
#
#  1 <= words.length <= 500
#  1 <= words[i].length <= 10
#  words[i] consists of lowercase English letters.
#  k is in the range [1, The number of unique words[i]]
#
#
#
#  Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
#  Related Topics Hash Table String Trie Sorting Heap (Priority Queue) Bucket
# Sort Counting 👍 4891 👎 261


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import heapq


class Solution:
  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    # 最小堆的方法。

    hashmap = {}
    heap = []
    for word in words:
      time = hashmap.get(word, 0)
      time = time + 1
      hashmap[word] = time

    for key, value in hashmap.items():
      heapq.heappush(heap, Node(key, value))
      if (len(heap) > k):
        heapq.heappop(heap)
    res = []
    while len(heap) > 0:
      temp = heapq.heappop(heap)
      res.append(temp.key)
    res.reverse()
    return res


class Node:
  def __init__(self, key, time):
    self.key = key
    self.time = time

  def __lt__(self, node):
    # 当出现次数相同的时候，当前文字code值大的在后面
    if self.time == node.time:
      return self.key > node.key
    # 当文字出现不同的时候，出现次数少的再后面
    return self.time < node.time
# leetcode submit region end(Prohibit modification and deletion)
