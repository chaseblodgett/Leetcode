// keep track of current page idx -> 0 initially
// have array of pages, where page idx maps to the string

type BrowserHistory struct {
    CurrentPage int
    History []string
}


func Constructor(homepage string) BrowserHistory {
    return BrowserHistory{
      History: []string{ homepage },
      CurrentPage: 0,
    }
}


// currPageIdx += 1
// set History[currPageIdx] = url ->
// set history = currHostory[:pageIdx] append(url)
func (this *BrowserHistory) Visit(url string)  {
    this.CurrentPage++
    this.History = append(this.History[:this.CurrentPage], url)
}

// setCurrPageIdx =  currPageidx - steps or 0 
// return history[currPageIdx] o(1)
func (this *BrowserHistory) Back(steps int) string {
    if this.CurrentPage - steps < 0{
      this.CurrentPage = 0
    } else {
      this.CurrentPage = this.CurrentPage - steps
    }
    return this.History[this.CurrentPage]
}

// if currPageIdx < len(history) -> move return history[pageIdx]
func (this *BrowserHistory) Forward(steps int) string {

    if this.CurrentPage + steps >= len(this.History){
      this.CurrentPage = len(this.History) - 1
    } else{
      this.CurrentPage = this.CurrentPage + steps
    }
    return this.History[this.CurrentPage]
}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */