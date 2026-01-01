func numberOfAlternatingGroups(colors []int) int {
    
    numAltGroups := 0
    n := len(colors)

    for i:=0; i < n; i++{
        if colors[(i-1 + n) % n] != colors[i] && colors[(i+1) % n] != colors[i]{
            numAltGroups++
        }
    }

    return numAltGroups
}