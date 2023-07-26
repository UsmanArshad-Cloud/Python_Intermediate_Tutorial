import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            print(f"Depositing {amount}")
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}")
                self.balance -= amount
            else:
                print("Insufficient balance.")

def perform_transactions(account):
    for _ in range(3):
        account.deposit(100)
        account.withdraw(50)

if __name__ == "__main__":
    account = BankAccount()

    # Create multiple threads to perform transactions
    threads = [threading.Thread(target=perform_transactions, args=(account,)) for _ in range(5)]

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Final balance:", account.balance)
