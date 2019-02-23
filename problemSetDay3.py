integer = int(input("Tell me a number."))

if integer % 2 == 0:
    print("That is even.")
else:
    print("Why did you put in an odd number? I don't like them.")

a = int(input("Tell me another number."))

if a % 2 == 0:
    print("That is even.")
else:
    print("Why did you put in an odd number? I don't like them.")

b = int(input("Tell me a third number."))

if b % 2 == 0:
    print("That is even.")
else:
    print("Why did you put in an odd number? I don't like them.")

if b % 2 == 0 and a % 2 == 0 and integer % 2 == 0:
    print("all your numbers are even! wow!")
else:
    print("You put at least one odd number, which I didn't like. :(")

print(" I didn't have time for part 3, as I needed to leave early. Sorry!")