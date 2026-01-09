func minCost(startPos []int, homePos []int, rowCosts []int, colCosts []int) int {
    // calculate row costs to get to home row from start row 
    // calculate col costs to get to home col from start col
    // sum them

    startRow := startPos[0]
    homeRow := homePos[0]
    rowSum := 0
    if startRow < homeRow{
        for i:=startRow+1;i<=homeRow;i++{
            rowSum += rowCosts[i]
        }
    } else{
        for i:=startRow-1;i>=homeRow;i--{
            rowSum += rowCosts[i]
        }
    }

    startCol := startPos[1]
    homeCol := homePos[1]
    colSum := 0
    if startCol < homeCol{
        for i:=startCol+1;i<=homeCol;i++{
            colSum += colCosts[i]
        }
    } else{
        for i:=startCol-1;i>=homeCol;i--{
            colSum += colCosts[i]
        }
    }

    return colSum + rowSum
}