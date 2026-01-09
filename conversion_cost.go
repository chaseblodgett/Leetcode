func equalSubstring(s string, t string, maxCost int) int {
    
    // for each index of s -> calculate how many operations you can do before money runs out
    // calculate the max length of substring
    // set max substring if it is larger
    maxLength := 0
    for i:=0;i<len(s);i++{
        cost := 0
        currLength := 0
        for i + currLength < len(s) && cost <= maxCost{
            cost += abs(s[i+currLength], t[i+currLength])
            if cost <= maxCost{
                currLength++
            }
        }
        maxLength = max(maxLength, currLength)
    }

    return maxLength
}

func abs(a, b byte) int {
    diff := int(a) - int(b)
    if diff < 0 {
        return -diff
    }
    return diff
}