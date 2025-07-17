/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    
    let i = 0;
    let max_length = 1;
    let curr_length = 1;
    for (; i < nums.length - 1; i++) {
        curr_length = 1;
        while(i < nums.length -1 && nums[i] < nums[i+1]){
            curr_length += 1;
            i += 1;
        }
        if(curr_length > max_length){
            max_length = curr_length;
        }
    }

    return max_length;

};