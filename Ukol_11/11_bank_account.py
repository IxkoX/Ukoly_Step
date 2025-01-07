class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        """
        Inicializace bankovního účtu.
        :param account_number: Číslo účtu (str nebo int).
        :param owner: Jméno majitele účtu (str).
        :param balance: Počáteční zůstatek (výchozí hodnota je 0).
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        Vloží peníze na účet.
        :param amount: Částka k vložení (kladné číslo).
        """
        if amount <= 0:
            print("Nelze vložit zápornou částku nebo nulu.")
            return
        self.balance += amount
        print(f"Vloženo: {amount}. Nový zůstatek: {self.balance}.")

    def withdraw(self, amount):
        """
        Odebere peníze z účtu.
        :param amount: Částka k odebrání.
        """
        if amount <= 0:
            print("Nelze odebrat zápornou částku nebo nulu.")
            return
        if amount > self.balance:
            print("Nedostatečné prostředky na účtu.")
            return
        self.balance -= amount
        print(f"Odebráno: {amount}. Nový zůstatek: {self.balance}.")

    def print_balance(self):
        """
        Tiskne aktuální zůstatek na účtu.
        """
        print(f"Číslo účtu: {self.account_number}, Majitel: {self.owner}, Zůstatek: {self.balance}.")


# Příklad použití
if __name__ == "__main__":
    account = BankAccount("123456789", "Jan Novák", 1000)
    account.print_balance()
    account.deposit(500)
    account.withdraw(300)
    account.withdraw(2000)
    account.print_balance()
