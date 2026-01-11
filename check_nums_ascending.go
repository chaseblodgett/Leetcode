import (
    "strings"
    "strconv"
  )
func areNumbersAscending(s string) bool {
    // split s into array with delimiter of " "
    // keep track of curr_elem -> -1 initiall
    // loop through the arr ->
      // if arr[i] is number and not > currElem -> return false
    
    // return true

    stringArr := strings.Split(s, " ")
    prevNum := -1
    for _,v := range stringArr{
      strNum,err := strconv.Atoi(v)
      if err == nil{
        if strNum <= prevNum{
          return false
        }
        prevNum = strNum
      }
    }

    return true
}