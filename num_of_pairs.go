import "strings"
func numOfPairs(nums []string, target string) int {
    
    // use a set
    // loop through nums 
        // if target.remove(nums[i]) is in set -> count++
        // add nums[i] to set
    
    // return count

    // set := make(map[string]struct{})
    count := 0
    for i:=0;i<len(nums);i++{
        for j:=0;j<len(nums);j++{
            if i != j && nums[i] + nums[j] == target{
                count++
            }
        }
        // _,exists := set[strings.Replace(target, nums[i], "", 1)]
        // if exists{
        //     count++
        // }
        // set[nums[i]] = struct{}{}
    }

    return count
}