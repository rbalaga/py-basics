name = "Ram"

greeting = f"Hello, {name}"

print(greeting) # Hello, Ram

name = "Suresh"

print (greeting) # Hello, Ram


print(f"Hello, {name}") # Hello, Suresh

name = "Ramesh"

print(f"Hello, {name}") # Hello, Ramesh


greeting1 = "Hello, {}"
name = "Bob"


message = greeting1.format(name)

print(message)

print(greeting.format(name))