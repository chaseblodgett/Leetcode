func integerBreak(n int) int {
    // 2 -> 1 * 1
    // 3 -> 2 * 1
    // 4 -> 2 * 2
    // 5 -> 3 * 2

    // loop from 2 to n/2
    // split n into chunks -> each chunk is (n / k)
    // for each remainder -> add 1 to remainder chunks
    // calculate the product from chunks
    // if new product is greater than curr product -> set max product

    maxProduct := 1

    for k:=2;k<=n;k++{
        currProduct := 1
        initialChunkSize := n / k
        remainder := n % k
        for i:=0;i<(k-remainder);i++{
            currProduct = currProduct * initialChunkSize
        }
        for j:=0;j<remainder;j++{
            currProduct = currProduct * (initialChunkSize + 1)
        }
        maxProduct = max(currProduct, maxProduct)
    }

    return maxProduct
}