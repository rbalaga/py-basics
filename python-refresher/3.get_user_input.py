name = input("Enter your name")

print("Hello, " + name)

size_input = input('How big is your house?')
square_feet = int(size_input)

squate_meters = square_feet / 10.8

print(f"{square_feet} square feet is {squate_meters} square meters.")

print(f"{square_feet} square feet is {squate_meters:.2f} square meters.")