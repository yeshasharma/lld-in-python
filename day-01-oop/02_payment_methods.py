from abc import ABC, abstractmethod


class InsufficientBalance(Exception):
    pass


class PaymentMethod(ABC):
    def __init__(self, owner: str) -> None:
        self._owner = owner

    @property
    def owner(self) -> str:
        return self._owner

    @abstractmethod
    def pay(self, amount: float) -> str: ...


class Wallet(PaymentMethod):
    def __init__(self, owner: str, balance: float) -> None:
        super().__init__(owner)
        self.__balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    def pay(self, amount: float) -> str:
        if amount > self.__balance:
            raise InsufficientBalance(f"{self.owner} has only {self.__balance}")
        self.__balance -= amount
        return f"Paid {amount} from {self.owner}'s wallet"


class UPI(PaymentMethod):
    def __init__(self, owner: str, upi_id: str) -> None:
        super().__init__(owner)
        self._upi_id = upi_id

    def pay(self, amount: float) -> str:
        return f"Paid {amount} via UPI {self._upi_id}"


class Card(PaymentMethod):
    def __init__(self, owner: str, last4: str) -> None:
        super().__init__(owner)
        self._last4 = last4

    def pay(self, amount: float) -> str:
        return f"Paid {amount} via card ending {self._last4}"


def checkout(method: PaymentMethod, amount: float) -> None:
    print(method.pay(amount))


if __name__ == "__main__":
    checkout(Wallet("Yesha", 500), 200)
    checkout(UPI("Rahul", "rahul@upi"), 300)
    checkout(Card("Priya", "4417"), 150)

    try:
        PaymentMethod("someone")  # type: ignore[abstract]
    except TypeError as error:
        print("Blocked:", error)
