import "fmt"

const MOD int64 = 1_000_000_007

func modPow(base, exp int64) int64 {
    result := int64(1)
    base %= MOD

    for exp > 0 {
        if exp&1 == 1 {
            result = (result * base) % MOD
        }
        base = (base * base) % MOD
        exp >>= 1
    }
    return result
}

func assignEdgeWeights(edges [][]int) int {
    // edges[0][0] = 1
    // find max depth
    // from max depth, determine num ways to reach it
    // at each edge -> 2 options (1 or 2)
    // if k = max_depth -> numWays = (2 ^ k) / 2


    // Step 1 -> find max depth
    // loop through edges -> if parent node not in set of parent nodes -> increase depth
    maxDepth := dfs(1, edges)
    fmt.Println(maxDepth)
    

    return int(modPow(2, int64(maxDepth-1)))

}
func dfs(node int, edges [][]int) int {
    maxDepth := 0
    for i := 0; i < len(edges); i++ {
        if edges[i][0] == node {
            depth := dfs(edges[i][1], edges) + 1
            if depth > maxDepth {
                maxDepth = depth
            }
        }
    }
    return maxDepth 
}
