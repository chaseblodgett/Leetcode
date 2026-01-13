import ( 
  "strings"
  "strconv"
)
// some sort of mapping
// cell -> value mapping?
// colRow -> val mapping? -> we know we have 26 cols, cells in format colRow
// A10 -> val or 0 if no elem exists
type Spreadsheet struct {
    CellValues map[string]int
}


func Constructor(rows int) Spreadsheet {
    return Spreadsheet{
      CellValues: make(map[string]int, rows*26),
    }
}


func (this *Spreadsheet) SetCell(cell string, value int)  {
    this.CellValues[cell] = value
}


func (this *Spreadsheet) ResetCell(cell string)  {
    this.CellValues[cell] = 0
}

// regex?

// loop from 1 to '+', create cell from that
// string function
func (this *Spreadsheet) GetValue(formula string) int {
    cells := strings.Split(formula, "+")

    valueOne := cells[0][1:]
    valueTwo := cells[1]

    sum := 0

    if _,ok := this.CellValues[valueOne]; !ok{
      toAdd, _ := strconv.Atoi(valueOne)
      sum += toAdd
    } else{
      sum += this.CellValues[valueOne]
    }

    if _,ok := this.CellValues[valueTwo]; !ok{
      toAdd, _ := strconv.Atoi(valueTwo)
      sum += toAdd
    } else{
      sum += this.CellValues[valueTwo]
    }

    return sum
}


/**
 * Your Spreadsheet object will be instantiated and called as such:
 * obj := Constructor(rows);
 * obj.SetCell(cell,value);
 * obj.ResetCell(cell);
 * param_3 := obj.GetValue(formula);
 */