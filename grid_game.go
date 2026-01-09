func gridGame(grid [][]int) int64 {
    // we want to find col that we go down that maximizes our score
    // sum all elems in second row
    // loop through grid
    // if cumSumRow1 + (secondRowSum - cumRowSum2) > maxScore
        // set k
    // if max column is col k 
    // -> sum all elems in row 0 where col j > k and sum all elems in row 1 where col j < k

    n := len(grid[0])
    firstRowScore := 0
    for i:=0;i<n;i++{
        firstRowScore += grid[0][i]
    }

    // find max(firstRowSum, secondRowSum) < maxScore
    maxScore := firstRowScore
    secondRowScore := 0
    for i:=0;i<n;i++{
        firstRowScore -= grid[0][i]
        currScore := max(secondRowScore, firstRowScore)
        if currScore < maxScore{
            maxScore = currScore
        }
        secondRowScore += grid[1][i]
    }

    return int64(maxScore)
}