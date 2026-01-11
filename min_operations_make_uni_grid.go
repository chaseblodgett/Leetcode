import "sort"
func minOperations(grid [][]int, x int) int {
    
    // not possible if diff between any 2 elems is not divisible by x
    // example:
        // x = 2 , elem1 = 3, elem2 = 6
        // 6 - 3 / 2 -> remainder of 1 -> not possible
    
    // num of operations -> find min, max elem, calculate middle point
    // for each elem in gird, calculate num operations to get to middle point
    // for each elem in grid, if abs(middlePoint - currElem) % x != 0 -> return -1

    // minElem + (abs(difference) / 2)

    vals := []int{}
    base := grid[0][0]

    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if (grid[i][j]-base)%x != 0 {
                return -1
            }
            vals = append(vals, (grid[i][j]-base)/x)
        }
    }
    sort.Ints(vals)
    median := vals[len(vals)/2]

    ops := 0
    for _, v := range vals {
        ops += abs(v, median)
    }
    return ops

}

func abs(a, b int) int{
    difference := a - b
    if difference < 0{
        return -difference
    }
    return difference
}