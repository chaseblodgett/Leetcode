// array to store balance
type Bank struct {
    Balance []int64
}

// return a new Bank struct with correct balance
func Constructor(balance []int64) Bank {
    return Bank{
      Balance: balance,
    }
}

// transfer from acc 1 -> acc2
func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    if !isValidAccount(account1, len(this.Balance)) || !isValidAccount(account2, len(this.Balance)){
      return false
    }

    if this.Withdraw(account1, money){
      return this.Deposit(account2, money)
    }

    return false
}

// check for account within range
// no checks on account money limiy
func (this *Bank) Deposit(account int, money int64) bool {
    if !isValidAccount(account, len(this.Balance)){
      return false
    }
    this.Balance[account-1] += money
    return true
}

// substract money from account
// if account out of range or balance[account] - money < 0 return false
// subtract money and return true
func (this *Bank) Withdraw(account int, money int64) bool {
    if !isValidAccount(account, len(this.Balance)) || this.Balance[account-1] - money < 0{
      return false
    }
    this.Balance[account-1] -= money
    return true
}

func isValidAccount(acc, balanceLength int) bool{
  return acc > 0 && acc <= balanceLength
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */