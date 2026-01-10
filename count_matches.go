func countMatches(items [][]string, ruleKey string, ruleValue string) int {
    // find certain idx to check i.e. 0,1 or 2 based on ruleKey
    // loop through items, check if val mataches ruleVal for ruleKey
    // increase count as we go

    var ruleIdx int
    if ruleKey == "type"{
        ruleIdx = 0
    } else if ruleKey == "color"{
        ruleIdx = 1
    } else {
        ruleIdx = 2
    }

    count := 0
    for i:=0;i<len(items);i++{
        if items[i][ruleIdx] == ruleValue{
            count++
        }
    }

    return count
}