/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {

    let pos = 0,
        idx = 0,
        temp;
    // 循环这个数组
    while (idx < nums.length) {
        //如果该次循环是非零数字的时候
        if (nums[idx] !== 0) {
            //当标记0的位置不是当前循环的位置的时刻，才进行转换
            //原因是我们认为pos标记的位置应该在当前循环的idx之前
            if (pos !== idx) {
                //临时变量存为0
                temp = nums[pos];
                //之前是0的位置存为当前的数字
                nums[pos] = nums[idx];
                //将当前的数字换做0
                nums[idx] = temp;
            }
            //将标记值+1；
            pos++;
        }
        //再次循环下一个数
        idx++;
    }
};
var nums = [2, 1, 0, 3, 12]
moveZeroes(nums);
console.log(nums);