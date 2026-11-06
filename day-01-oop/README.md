# Day 1: OOP Through a Designer's Eyes

Every OOP pillar answers one design question:

| Pillar | Design question |
|---|---|
| Encapsulation | Who owns this data, and how can it change? |
| Abstraction | How much must the caller know? |
| Inheritance | Is it truly an "is-a"? |
| Polymorphism | When a new type arrives, how much old code changes? |

## Files (in video order)
1. `00_class_object.py`: class vs object, and why public data is risky
2. `01_encapsulation.py`: data and its rules live together
3. `02_payment_methods.py`: abstraction, inheritance, polymorphism
4. `03_protocol.py`: duck typing with `typing.Protocol`

## Your turn
Add a credit limit to `Card` and raise a custom exception when a payment crosses it.
Then answer: which pillar did you use, and where?
Try it before you look at anyone else's solution.
