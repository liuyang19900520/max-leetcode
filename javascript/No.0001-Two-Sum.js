//Given an array of integers nums and an integer target, return indices of the t
//wo numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may n
//ot use the same element twice.
//
// You can return the answer in any order.
//
//
// Example 1:
//
//
//Input: nums = [2,7,11,15], target = 9
//Output: [0,1]
//Output: Because nums[0] + nums[1] == 9, we return [0, 1].
//
//
// Example 2:
//
//
//Input: nums = [3,2,4], target = 6
//Output: [1,2]
//
//
// Example 3:
//
//
//Input: nums = [3,3], target = 6
//Output: [0,1]
//
//
//
// Constraints:
//
//
// 2 <= nums.length <= 103
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.
//
// Related Topics Array Hash Table
// 👍 20284 👎 716


//leetcode submit region begin(Prohibit modification and deletion)
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const comp = {};
    // 循环数组
    for(let i=0; i<nums.length; i++){
        //判断comp中是否存在当前index对应的num对象，如果有就返回数组
        //该数组就是元素目标数组
        if(comp[nums[i] ]>=0){
            return [ comp[nums[i] ] , i]
        }
        //将当前循环的下标i作为值放入comp中，对应的key为当前index对应元素num
        comp[target-nums[i]] = i
    }
};
//leetcode submit region end(Prohibit modification and deletion)
