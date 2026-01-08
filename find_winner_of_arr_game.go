func getWinner(arr []int, k int) int {
    

    // if k >= len(arr) -> return max elem in arr
    // otherwise -> 
        // loop through arr
        // keep track of current_max
        // keep track of win streak -> if winStreak >= k return currMax
    
    winStreak := 0
    maxElem := arr[0]
    for i:=1;i<len(arr);i++{

        if winStreak >= k{
            return maxElem
        } else if arr[i] > maxElem{
            winStreak = 1
            maxElem = arr[i]
        } else {
            winStreak++
        }
    }

    return maxElem

}