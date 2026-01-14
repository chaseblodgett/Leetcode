// constructor -> initialize class object

// adjacentSum -> return top, left, bottom, right values next to value

// diaganolSum -> return diaganol adjacent values next to value

// any more requirements?

// Have grid be 2d int array
type NeighborSum struct {
    AdjacentMap map[int]int
    DiagonalMap map[int]int
}

// create the mapping of adjacent sums and diaganol sums
func Constructor(grid [][]int) NeighborSum {
    n := len(grid)
    mapA := make(map[int]int)
    mapD := make(map[int]int)
    for row:=0; row < n; row++{
        for col :=0; col < n; col++{
            up := getValue(row-1, col, n, grid)
            down := getValue(row+1, col, n, grid)
            left := getValue(row, col-1, n, grid)
            right := getValue(row, col+1, n, grid)
            mapA[grid[row][col]] = up + down + left + right

            upLeft := getValue(row-1, col-1, n, grid)
            upRight := getValue(row-1, col+1, n, grid)
            downLeft := getValue(row+1, col-1, n, grid)
            downRight := getValue(row+1, col+1, n, grid)
            mapD[grid[row][col]] = upLeft + upRight + downLeft + downRight
        }
    }

    return NeighborSum{
        AdjacentMap: mapA,
        DiagonalMap: mapD,
    }
}

// finding row/col of value -> sum adjacent elems
//
func (this *NeighborSum) AdjacentSum(value int) int {
    return this.AdjacentMap[value]
}


func (this *NeighborSum) DiagonalSum(value int) int {
    return this.DiagonalMap[value]
}

func getValue(i int, j int, n int, grid [][] int) int{
    if i < 0 || j < 0 || j >= n || i >= n{
        return 0
    }
    return grid[i][j]
}

// calculate idx of value dynamically 

// getIndex helper function -> return index of certain value without looping
// Need to calculate row, col
// row = value / n
// col = value % n



/**
 * Your NeighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
 */