func missingRolls(rolls []int, mean int, n int) []int {
    // need to find n numbers to satisfy the mean in addition to rolls
    // mean = sum(rolls) + sum(answer) / (n + m)
    // mean * (n + m) - sum(rolls) = sum(answer)
    // base elem of answer array -> sum(answer) / 2 -> add leftovers to other elems if possible

    m := len(rolls)
    sumRolls := 0
    for i:=0;i<m;i++{
        sumRolls += rolls[i]
    }

    sumAnswer := mean * (n+m) - sumRolls
    answer := []int{}

    baseElem := sumAnswer / n
    remainderVal := sumAnswer % n

    if baseElem > 6 || baseElem <= 0{
        return answer
    } 

    if baseElem == 6 && remainderVal > 0{
        return answer
    }

    for i:=0;i<n;i++{
        if i < remainderVal{
            answer = append(answer, baseElem+1)
        } else{
            answer = append(answer, baseElem)
        }
    }

    return answer
}