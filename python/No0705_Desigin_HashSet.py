# Design a HashSet without using any built-in hash table libraries.
#
#  Implement MyHashSet class:
#
#
#  void add(key) Inserts the value key into the HashSet.
#  bool contains(key) Returns whether the value key exists in the HashSet or
# not.
#  void remove(key) Removes the value key in the HashSet. If key does not exist
# in the HashSet, do nothing.
#
#
#
#  Example 1:
#
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
#
#  Constraints:
#
#
#  0 <= key <= 10⁶
#  At most 10⁴ calls will be made to add, remove, and contains.
#
#  Related Topics Array Hash Table Linked List Design Hash Function 👍 2106 👎 2
# 08


# leetcode submit region begin(Prohibit modification and deletion)
class MyHashSet:

  def __init__(self):
    #创建一个10的六次方的大小的数组，每个位置都放上默认值false
    self.val = [False] * (10 ** 6 + 1)

  def add(self, key: int) -> None:
    # 添加一个设为true
    self.val[key] = True

  def remove(self, key: int) -> None:
    # 删除一个设为false
    self.val[key] = False

  def contains(self, key: int) -> bool:
    # 确认都判断key是否为true
    return self.val[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)
