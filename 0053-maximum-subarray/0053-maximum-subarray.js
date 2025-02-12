/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let min_sum = 0;
    let running_sum = 0;
    let max_sum = Math.max(...nums);

    for(let num of nums){
        running_sum += num;
        max_sum = Math.max(max_sum, running_sum - min_sum);
        min_sum = Math.min(running_sum, min_sum);

    }


    return max_sum;
};