

func smallerNumbersThanCurrent(nums []int) []int {


    // set up return arr
    // loop through arr
    // for each elem loop through arr and count how many less than nums[i]

    ret := []int{}
    for i:=0; i<len(nums); i++{
        count := 0
        for j:=0; j < len(nums); j++{
            if i != j && nums[j] < nums[i]{
                count++
            }
        }
        ret = append(ret, count)
    }

    return ret
}