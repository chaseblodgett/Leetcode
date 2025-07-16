/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */


var findMaxAverage = function(nums, k) {
    let sum = nums.slice(0, k).reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    let max_sum = sum;
    for(let i = k; i < nums.length; i++){
        sum -= nums[i-k];
        sum += nums[i];
        if(sum > max_sum){
            max_sum = sum;
        }
    }
   
    return max_sum / k;
    
};