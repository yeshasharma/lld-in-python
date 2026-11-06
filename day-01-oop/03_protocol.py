from typing import Protocol


class Payable(Protocol):
    def pay(self, amount: float) -> str: ...


class GiftCard:
    def pay(self, amount: float) -> str:
        return f"Paid {amount} via gift card"


def quick_pay(method: Payable, amount: float) -> None:
    print(method.pay(amount))


if __name__ == "__main__":
    quick_pay(GiftCard(), 100)
