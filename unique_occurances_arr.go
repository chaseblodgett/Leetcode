func uniqueOccurrences(arr []int) bool {
    // set up hash map
    // keys are elems of arr -> vals are number of occurances
    // loop through key val pairs -> add to set of occurances
    // if an occurance is in set -> return false
    // if we reach end of loop return true

    mp := make(map[int]int)

    for i:=0;i<len(arr);i++{
        mp[arr[i]] += 1
    }

    set := make(map[int]struct{})

    for _,val := range mp{
        if _, ok := set[val]; ok {
            return false
        }
        set[val] = struct{}{}
    }

    return true
}