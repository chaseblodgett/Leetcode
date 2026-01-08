import "sort"
func absDifference(nums []int, k int) int {
    // find k largest
    // find k smallest
    // return abs(sum(large) - sum(small))

    // sort nums
    // sum elements 0 - k -> kLargestSum
    // sum elements len(nums)-k -> len(nums) -> kSmallestSum

    sort.Ints(nums)

    kLargestSum := 0
    kSmallestSum := 0

    for i:=0; i<len(nums);i++{
        if i < k{
            kLargestSum += nums[i]
        }
        if i >= len(nums)-k{
            kSmallestSum += nums[i]
        }
    }

    difference := kLargestSum - kSmallestSum

    if difference < 0{
        return -difference
    }
    return difference
}