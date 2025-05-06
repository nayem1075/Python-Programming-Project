
from collections import deque

bank = deque(["Rahim","Karim","Bijoy"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

if not bank:
    print("No Person left")

