"""
## 2. Bank Account Class  *(Medium)*

=================================================
BANK ACCOUNT CLASS
=================================================

Problem Statement:
Write a Python CLASS called `BankAccount`
that represents a simple bank account. Each
account has an account holder's name, a
unique account number, and a balance that
starts at 0 unless an opening balance is
given.

The class must support deposits, withdrawals,
and balance checks. Reject invalid operations
(negative amounts, overdrafts) by printing a
clear message — do NOT crash.

-------------------------------------------------
Instructions:
1. Define a class:
      class BankAccount:
2. Constructor:
      def __init__(self, name, account_number,
                   opening_balance=0):
          - validate that opening_balance >= 0
          - store name, account_number, balance
            on `self`
3. Instance methods:
      - deposit(self, amount)
            * reject amount <= 0 with a message
            * otherwise add to balance
      - withdraw(self, amount)
            * reject amount <= 0
            * reject if amount > balance
            * otherwise subtract from balance
      - get_balance(self)
            * return the current balance
      - __str__(self)
            * return a friendly string like:
              "Account[001 - Alice]: $500"
4. In the driver code:
      - create AT LEAST TWO accounts
      - perform some valid deposits / withdraws
      - perform AT LEAST ONE invalid operation
        (negative amount or overdraft) on each
        account to show the rejection message
      - print each account using print(acc),
        which triggers __str__
5. Do NOT use:
   - class-level mutable defaults (e.g. a list
     as default argument)
   - global variables

-------------------------------------------------
Input Example:
a1 = BankAccount("Alice", "001", 500)
a2 = BankAccount("Bob",   "002")
a1.deposit(200)
a1.withdraw(100)
a1.withdraw(2000)   # overdraft -> rejected
a2.deposit(-50)     # invalid   -> rejected
a2.deposit(300)

Output Example:
Insufficient funds for Alice (balance=600, asked=2000)
Deposit amount must be > 0 (got -50)
Account[001 - Alice]: $600
Account[002 - Bob]:   $300

-------------------------------------------------
Explanation:
- `self.balance` is independent for every
  object, so Alice and Bob keep separate
  balances.
- Validation in `deposit` and `withdraw` shows
  how methods use `self` to read AND update
  state on the same object.
- `__str__` returns the human-readable form
  used by print().
=================================================

"""
class BankAccount:
    def __init__(self, name: str, account_number: str, opening_balance: float = 0.0):
        # Validate that opening balance is non-negative
        if opening_balance < 0:
            print("Initial balance cannot be negative.")
            self.balance = 0.0
        else:
            self.balance = float(opening_balance)
            
        # Store name and account number on self
        self.name = name
        self.account_number = account_number

    def deposit(self, amount: float):
        # Reject amount <= 0 with a message
        if amount <= 0:
            print(f"Deposit amount must be > 0 (got {amount})")
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        # Reject amount <= 0
        if amount <= 0:
            print(f"Withdrawal amount must be > 0 (got {amount})")
        # Reject if amount > balance (overdraft)
        elif amount > self.balance:
            print(f"Insufficient funds for {self.name} (balance={self.balance}, asked={amount})")
        else:
            self.balance -= amount

    def get_balance(self) -> float:
        # Return the current balance
        return self.balance

    def __str__(self) -> str:
        # Return a friendly string representation
        return f"Account[{self.account_number} - {self.name}]: ${self.balance:.0f}"


# --- Driver Code ---
if __name__ == "__main__":
    # Create AT LEAST TWO accounts
    a1 = BankAccount("Alice", "001", 500)
    a2 = BankAccount("Bob", "002")

    # Perform valid operations
    a1.deposit(200)
    a2.deposit(300)

    # Perform AT LEAST ONE invalid operation (overdraft & negative)
    a1.withdraw(100)
    a1.withdraw(2000)  # Overdraft -> rejected
    a2.withdraw(-50)   # Invalid -> rejected

    # Print each account using print(), which triggers __str__
    print(a1)
    print(a2)

