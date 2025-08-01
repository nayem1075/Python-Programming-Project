#Parent class, Super class, Base class
class Phone :
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

#Child class,Sub class, Derived class
class Samsung (Phone) :
      #Here call() and message ()

    def photo(self):
        print("You can take photo")

print(issubclass(Samsung,Phone))
print(issubclass(Phone,Samsung))

s = Samsung()
s.call()
s.message()
s.photo()