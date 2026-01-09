func findShortestSubArray(nums []int) int {
    // find degree of nums
    // for each elem loop through nums until degree is met with that elem or end of nums
    // if we reach same degree set max length if needed otherwise continue

    mp := make(map[int]int)

    for i:=0;i<len(nums);i++{
        mp[nums[i]]++
    }

    degree := 1
    for _,value := range mp{
        if value > degree{
            degree = value
        }
    }

    minSubarray := len(nums)
    for i:=0;i<len(nums);i++{
        currDegree := 1
        idx := i + 1
        for idx < len(nums) && currDegree < degree{
            if nums[idx] == nums[i]{
                currDegree++
            }
            idx++
        }
        if currDegree == degree{
            minSubarray = min(minSubarray, idx - i)
        }
    }

    return minSubarray
}