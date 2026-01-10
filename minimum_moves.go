func minimumMoves(s string) int {
    
    // find number of groups to flip
    // if in i:i+3 there is an X -> count++
    // keep track of count, loop through s by 3

    count := 0
    idx := 0
    for idx < len(s){

        if s[idx] == 'X'{
            idx += 3
            count++
        } else {
            idx += 1
        }
    }

    return count
}