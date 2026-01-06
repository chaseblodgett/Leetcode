import "strconv"

func isIntegerString(s string) bool {
    _, err := strconv.Atoi(s)
    return err == nil
}
func calPoints(operations []string) int {
    record := []int{}

    for i:=0; i < len(operations); i++{

        if isIntegerString(operations[i]){
            val, _ := strconv.Atoi(operations[i])
            record = append(record, val)
        } else if operations[i] == "+"{
            record = append(record, record[len(record)-2] + record[len(record) -1])
        } else if operations[i] == "D"{
            record = append(record, record[len(record)-1] * 2)
        } else if operations[i] == "C"{
            record = append(record[:len(record)-1])
        }
    }
    
    arrSum := 0
    for i:=0; i < len(record); i++{
        arrSum += record[i]
    }

    return arrSum
}