func absInt(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func scoreOfString(s string) int {

    runes := []rune(s)
    score := 0
    for i := 0; i < len(runes)-1; i++ {
        score += absInt(int(runes[i] - runes[i+1]))
    }

    return score
}