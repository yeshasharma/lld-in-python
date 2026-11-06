class InsufficientBalance(Exception):
    pass


class Wallet:
    def __init__(self, owner: str, balance: float) -> None:
        self._owner = owner
        self.__balance = balance

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return self.__balance

    def pay(self, amount: float) -> str:
        if amount > self.__balance:
            raise InsufficientBalance(f"{self._owner} has only {self.__balance}")
        self.__balance -= amount
        return f"Paid {amount} from {self._owner}'s wallet"


if __name__ == "__main__":
    wallet = Wallet("Yesha", 500)
    print(wallet.pay(200))
    print("Balance:", wallet.balance)

    try:
        wallet.balance = -5000  # type: ignore[misc]
    except AttributeError as error:
        print("Blocked:", error)
