from datetime import datetime

class Transaction:
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()
        
    def __str__(self):
        sign = "+" if self.transaction_type == "deposit" else "-"
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] {self.transaction_type}: {sign}{self.amount:.2f}"
    
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the availble price."""
    pass

class Wallet:
    def __init__(self, AccountHolder: str, balance: float = 0.0):
        self.AccountHolder = AccountHolder
        self._balance = balance
        self._history = []
        
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amounthas to be a positive number, not a negative one..")
        self._balance += amount
        self._history.append(Transaction(amount, "deposit"))
        
    def withdraw(self, amount:float):
        if amount <= 0:
            raise ValueError("Your amount is negative, you have to have a positive amount..")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Impossible to withdraw {amount:.2f}, while your balance is {self._balance:.2f} lol.."
                
            )
        self._balance -= amount
        self._history.append(Transaction(amount, "withdrawal.."))
        
    def Display_History(self):
        for transaction_type in self._history:
            print(transaction_type)
    def get_balance(self) -> float:
        return self._balance
    
if __name__ == "__main__":
    w = Wallet("Rorisang Madikgetla", balance=7800000.97)
    w.deposit(100000)
    w.withdraw(78000)
    print(f"Balance: {w.get_balance():.2f}")
    w.Display_History()
    