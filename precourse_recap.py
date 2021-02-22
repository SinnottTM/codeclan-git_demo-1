username = input("Enter username: ")
print("I have a question for you " + username +".")
random_number = float(input("Could you pick a number between 1 and 10 please? Your number is... "))
if random_number > 0 and random_number < 10:
    print("You can follow instructions, well done!")
else:
    print("WRONG! Just had to try to be clever, didn't you?")