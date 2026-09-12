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
    