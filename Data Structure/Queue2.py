
from collections import deque

bank = deque(["Rahim","Karim","Jamir"])

print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()

if not bank :
    print("No person left")