import "fmt"
func checkZeroOnes(s string) bool {
    // find max length of ones
    // find max length of zeros
    // if ones > zeros return true else return false
    // set up 3 vars -> maxOnes, maxZeros, currStreak

    maxOnes := 0
    maxZeros := 0
    currStreak := 1

    for i:=1;i<len(s);i++{
        if s[i] != s[i-1] && s[i] == '1'{
            maxZeros = max(currStreak, maxZeros)
            currStreak = 1
        } else if s[i] != s[i-1] && s[i] == '0'{
            maxOnes = max(currStreak, maxOnes)
            currStreak = 1
        } else {
            currStreak += 1
        }
    }

    if s[len(s)-1] == '1'{
        maxOnes = max(currStreak, maxOnes)
    } else{
        maxZeros = max(currStreak, maxZeros)
    }
    
    return maxOnes > maxZeros
}