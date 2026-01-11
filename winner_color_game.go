import "fmt"
func winnerOfGame(colors string) bool {
    // calculate total number of moves each player can make
    // Alice score = length of contiguous substrings > 3 (-2 for each substring)
    // after calculating possible number of moves for each player
    // if alice moves > bob moves -> return true else return false

    // loop through string, calculate scores

    aliceScore := 0
    bobScore := 0
    currSubLength := 1

    for i:=1;i<len(colors);i++{
      if colors[i] != colors[i-1]{
        if colors[i] == 'A' && currSubLength >= 3{
          bobScore += currSubLength - 2
        } else if colors[i] == 'B' && currSubLength >= 3{
          aliceScore += currSubLength - 2
        }
        currSubLength = 1
      } else {
        currSubLength++
      }
    }

    if currSubLength >= 3 {
      if colors[len(colors) - 1] == 'B'{
        bobScore += currSubLength - 2
      } else{
        aliceScore += currSubLength - 2
      }
    }

    // fmt.Println(aliceScore)
    // fmt.Println(bobScore)
    return aliceScore > bobScore
}