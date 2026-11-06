class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance


if __name__ == "__main__":
    first = Wallet("Yesha", 500)
    second = Wallet("Rahul", 1000)
    print(first.balance, second.balance)

    first.balance = -5000
    print("Nobody stopped this:", first.balance)
