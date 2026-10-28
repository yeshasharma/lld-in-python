# LLD in Python

Code for the **LLD in Python** YouTube series by **Learn with Yesha**: 90 days, one video a day, explained in Hinglish.

> **Think. Don't memorize.**
> This series doesn't hand you answers to memorize. It teaches you how to *think* through any Low Level Design problem, so you can handle the ones you've never seen.

📺 **Playlist:** _coming soon_

---

## What makes this series different

**1. One way to think through every problem: SOCHO**

| Step | What you do |
|---|---|
| **S**cope | Clarify requirements: what to build, what not to build |
| **O**bjects | Find the entities and what each one is responsible for |
| **C**onnections | Decide relationships: is-a, has-a, uses |
| **H**ow it changes | Spot what can change and design for it (this is where patterns come from) |
| **O**utput | Write the code, walk through it, handle follow-up requirements |

**2. Patterns are discovered, not memorized.** Every pattern shows up inside a real problem, only after you feel the pain it solves.

**3. Pythonic design.** `dataclass`, `Protocol`, `Enum`, type hints and `mypy` used as design tools, not Java translated to Python.

**4. LLD → HLD.** Every case study ends with *Scale It*: what breaks at 1 lakh users? In Month 3, the same designs grow into databases, distributed locks, caches and message brokers.

---

## How to use this repo

A new folder is added here on the day its video goes live. Each day has its own folder:

```
day-XX-topic/
├── README.md      # what the video covers + your homework
├── *.py           # code from the video, in the order it appears
└── diagrams/      # editable .excalidraw diagrams (when the video has them)
```

1. Watch the video.
2. **Before** opening the code, try the homework yourself. The thinking is the point.
3. Then compare with the code here.

### Requirements
- Python 3.12+
- Optional: `pip install mypy pytest` (used from Day 3 onwards)

---

## Roadmap

### Month 1: Tools, Thinking & First Problems
| Day | Topic |
|---|---|
| 0 | Series Intro |
| 1 | OOP Through a Designer's Eyes |
| 2 | Is-a, Has-a or Uses? Choosing the Right Relationship |
| 3 | 5 Python Tools Every LLD Needs |
| 4 | SRP & OCP Are Questions, Not Rules |
| 5 | Tests Pass, Prod Crashes: LSP & ISP |
| 6 | Dependency Injection Without a Framework |
| 7 | UML in 5 Minutes: Class & Sequence Diagrams |
| 8 | SOCHO: How to Think Through Any LLD Problem |
| 9 | Finding Objects & Connections: Library System |
| 10 | Designing for Change: Library System Code |
| 11 | Tic Tac Toe: Thinking It Through |
| 12 | Snake & Ladder: Thinking It Through |
| 13 | Parking Lot: Think Before You Code |
| 14 | Parking Lot: Code, Follow-ups & Scale It |
| 15 | Vending Machine: When if-else Becomes a State Machine |
| 16 | Online Auction: Discovering the Observer Pattern |
| 17 | Logger Framework: Chain of Responsibility & Singleton |
| 18 | Text Editor Undo/Redo: Command & Memento |
| 19 | File System: Thinking in Trees |
| 20 | Coffee Order Customization: Decorator & Builder |
| 21 | One Interface, Many Payment Providers |
| 22 | The Pattern Map: Which Change Needs Which Pattern |
| 23 | Spot the Pattern: 10 Scenarios Drill |
| 24 | Concurrency for LLD: Race Conditions, Locks & GIL |
| 25 | Producer-Consumer, Threads vs asyncio |
| 26 | Thread-safe Design: Where Is the Shared State? |
| 27 | LRU Cache: Choosing the Right Data Structure |
| 28 | Rate Limiter: Token Bucket vs Sliding Window |
| 29 | Elevator System: Thinking It Through |
| 30 | Elevator System: Code, Scheduling & Scale It |

### Month 2: Real-World Problems
| Day | Topic |
|---|---|
| 31 | Splitwise: Thinking It Through |
| 32 | Splitwise: Code & Simplify Debts |
| 33 | BookMyShow: Thinking It Through |
| 34 | BookMyShow: Code & Seat Locking |
| 35 | Chess: Thinking It Through |
| 36 | Chess: Code & Move Validation |
| 37 | ATM Machine: Thinking It Through |
| 38 | Hotel Booking: Preventing Double Booking |
| 39 | Car Rental System: Thinking It Through |
| 40 | Food Delivery: Thinking It Through |
| 41 | Food Delivery: Code & Delivery Assignment |
| 42 | Uber: Thinking It Through |
| 43 | Uber: Code, Matching & Surge Pricing |
| 44 | Notification Service: Thinking It Through |
| 45 | Pub-Sub & Message Queue from Scratch |
| 46 | Task Scheduler: Thinking It Through |
| 47 | In-memory Key-Value Store with TTL |
| 48 | E-commerce Cart & Order Flow |
| 49 | Coupon & Discount Engine |
| 50 | Inventory Management: Thinking It Through |
| 51 | Payment Gateway: Idempotency, Retries & Refunds |
| 52 | Stack Overflow: Thinking It Through |
| 53 | Twitter Feed: Pull vs Push |
| 54 | Meeting Room Scheduler & Calendar |
| 55 | Stock Exchange Order Matching Engine |
| 56 | Digital Wallet: Ledger & Concurrency |
| 57 | Cricbuzz Live Scoreboard |
| 58 | Airline Booking: Thinking It Through |
| 59 | 28 Problems, Same Mistakes: What Not to Do |
| 60 | Month 2 Recap: Problem → Pattern → Scale Map |

### Month 3: Machine Coding & LLD → HLD
| Day | Topic |
|---|---|
| 61 | Machine Coding Round: Your 90-Minute Plan |
| 62 | Project Structure & pytest Under Time Pressure |
| 63 | Handling Follow-up Requirements |
| 64 | Thinking Out Loud & Explaining Trade-offs |
| 65 | Live 90-Min Machine Coding: Parking Lot |
| 66 | Live 90-Min Machine Coding: Splitwise |
| 67 | Self-review Checklist & Code Smells |
| 68 | The Hidden Assumptions in Your LLD |
| 69 | From Repository to Database |
| 70 | From Lock to Distributed Lock |
| 71 | From Observer to Message Broker |
| 72 | From LRU Cache to Distributed Cache |
| 73 | Distributed Rate Limiter |
| 74 | Singletons & IDs Across Many Servers |
| 75 | From Classes to Service Boundaries |
| 76 | From Interfaces to APIs |
| 77 | Retry, Idempotency & Circuit Breaker |
| 78 | BookMyShow: From LLD to HLD |
| 79 | Uber: From LLD to HLD |
| 80 | Notification System: From LLD to HLD |
| 81 | Twitter Feed: From LLD to HLD |
| 82 | Mock Interview: Uber |
| 83 | Mock Interview: BookMyShow |
| 84 | Mock Interview: Rate Limiter |
| 85 | Mock Interview: Elevator |
| 86 | Mock Interview: Food Delivery |
| 87 | Mock Interview: Digital Wallet |
| 88 | Top LLD Interview Questions: Rapid-fire |
| 89 | How to Keep Practicing After This Series |
| 90 | Wrap-up & What's Next: HLD |

---

## Contributing
Found a bug or have a cleaner design? Open an issue or a PR. Explaining *why* your design is better is more valuable than the code itself.

## License
[MIT](LICENSE)
