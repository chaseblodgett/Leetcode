func maximumDifference(nums []int) int {

   // loop through nums
    // loop from i + 1 through nums
        // set maxDiff(nums[j] - nums[i])

    // if maxDiff > 0 return maxDiff else -1

    maxDiff := -1
    for i:=0;i<len(nums);i++{
        for j:=i+1;j<len(nums);j++{
            maxDiff = max(maxDiff, nums[j] - nums[i])
        }
    }

    if maxDiff > 0{
        return maxDiff
    }
    return -1
}