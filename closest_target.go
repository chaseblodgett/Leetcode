func closestTarget(words []string, target string, startIndex int) int {
    
    n := len(words)
    left := startIndex
    right := startIndex

    for i:=0; i<n; i++{
        if words[left] == target || words[right] == target{
            return i
        }
        left = (left - 1 + n) % n
        right = (right + 1) % n
    }

    return -1
}