number_one = float(input("The first number is "))
number_two = float(input("The second number is "))

operation = input("The operation is ").lower()

if operation == "s":
    print("The sum is {}".format(number_one + number_two))
elif operation == "r":
    print("The rest is {}".format(number_one - number_two))
elif operation == "m":
    print("The multiplication is {}".format(number_one * number_two))
elif operation == "d":
    print("The division is {}".format(number_one / number_two))
elif operation == "p":
    print("The power is {}".format(number_one ** number_two))
else:
    print("The operation is not valid")
