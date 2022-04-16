letter = input("The letter is ").lower()

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("{} is a vocal".format(letter))
else:
    print("{} is not a vocal".format(letter))
