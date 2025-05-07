
#xargs
# We can pass more argument
def student(*details) :
    print(details)

student(100,"Rahim")
student("Nayem",101,3.86)

def information(*details) :
    print(details[0])

# Here print 0 index
information(101,102,103,104,105)

