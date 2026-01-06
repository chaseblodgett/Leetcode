func majorityFrequencyGroup(s string) string {
    
    mp := make(map[rune]int)

    for _,r := range s{
        mp[r]++
    }

    // mp = { a : 3, b : 3, c : 2, d: 4, e : 1}
    // freqMap = { 3 : "ab", 2 : "c", 4: "d", 1 : "e"}

    freqMap := make(map[int]string)

    for key,val := range mp{
        freqMap[val] += string(key)
    }

    maxKey := ""
    for key,val := range freqMap{
        if len([]rune(val)) > len([]rune(maxKey)){
            maxKey = val
        } else if len([]rune(val)) == len([]rune(maxKey)) && key > mp[rune(maxKey[0])]{
            maxKey = val
        }
    }

    return maxKey
}