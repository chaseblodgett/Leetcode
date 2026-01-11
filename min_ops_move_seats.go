import "sort"
func minMovesToSeat(seats []int, students []int) int {
    // for each student need to find closest seat
    // add abs(distance from seat) to total
    // return total

    // sort seats and students
    // for each student, i -> total += abs(seats[i], students[i])
    sort.Ints(seats)
    sort.Ints(students)
    total := 0
    for i:=0;i<len(students);i++{
        total += abs(students[i], seats[i])
    }

    return total
}

func abs(a, b int) int{
    difference := a - b
    if difference < 0{
        return -difference
    }
    return difference
}