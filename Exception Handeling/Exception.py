def Voter(age) :
    if age < 18 :
        raise ValueError("Invalid voter")
    return "You are allowed to vote"

try :
    a = int(input("Enter your age : "))
    result = Voter(a)
    print(result)
except ValueError as e :
    print(e)