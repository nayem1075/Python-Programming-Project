
try:
    text = "Nayem"
    print(text[5])
except IndexError:
    print("We can't print 5th number index in this text")
finally :
    print("Successful")
