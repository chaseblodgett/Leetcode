import (
    "sort"
    "fmt" 
)

type Query struct {
    value int
    idx   int
}

func maximumBeauty(items [][]int, queries []int) []int {
    // for each query ->
        // 1. find all items with price < query
        // 2. For each of those items, find max beauty
        // 3. Append that to answer array

    // set up answer arr

    // sort queries
    // sort items

    // loop through queries
        // loop while queries [i] < items[trackIdx]
            // maxBeauty = max(maxBeauty, items[j][1])
    
    sort.Slice(items, func(i, j int) bool {
        return items[i][0] < items[j][0]
    })
    qs := make([]Query, len(queries))
    for i, v := range queries {
        qs[i] = Query{value: v, idx: i}
    }

    sort.Slice(qs, func(i, j int) bool {
        return qs[i].value < qs[j].value
    })

    answer := make([]int, len(queries))
    itemsIdx := 0
    maxBeauty := 0

    fmt.Println(items)
    for i := 0; i < len(qs); i++ {
        for itemsIdx < len(items) && qs[i].value >= items[itemsIdx][0] {
            maxBeauty = max(maxBeauty, items[itemsIdx][1])
            itemsIdx++
        }
    answer[qs[i].idx] = maxBeauty
    }

    return answer
}