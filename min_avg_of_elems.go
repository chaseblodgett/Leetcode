import (
    "sort"
    "fmt"
)

func minimumAverage(nums []int) float64 {
    
    sort.Ints(nums[:])
    var average float64 = float64(nums[len(nums)-1] * 2)

    for i:=0; i<len(nums)/2; i++{
        left := float64(nums[i])
        right := float64(nums[len(nums)-i-1])
        average = min(average, (left+right)/2)
    }
    return average
}