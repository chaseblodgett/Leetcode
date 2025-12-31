import (
    "sort"
    "fmt"
)
func minimumDifference(nums []int, k int) int {
    if k <= 1 {
        return 0
    }
    sort.Ints(nums[:])
    ret := nums[len(nums) -1] - nums[0]

    for i := 0; i+k-1 < len(nums); i++ {
        ret = min(ret, nums[i+k-1] - nums[i])
    }

    return ret
}