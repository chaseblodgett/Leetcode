func semiOrderedPermutation(nums []int) int {
    
    // find index of 1 -> k
    // find index of len(nums) -> j
    
    // numOperations = k + (n - j + 1) - 1 if k > j else 0
    n := len(nums)
    k := 0
    j := 0

    for i:= 0; i< len(nums); i++{
        if nums[i] == 1{
            k = i
        } else if nums[i] == n{
            j = i + 1
        }
    }

    if k == 0 && j == n{
        return 0
    } else if k >= j{
        return k + (n - j) - 1
    } else {
        return k + (n - j)
    }
}