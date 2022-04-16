age = int(input("My age is "))

if age <= 0:
    print("You are not born yet")
elif age <= 2:
    print("You are a baby")
elif age <= 18:
    print("You are a minor")
elif age > 18:
    print("You are an adult")
elif age > 65:
    print("You are an elder")
elif age > 100:
    print("You are a very old")
elif age > 1000:
    print("You are a god")
else:
    print("Your age is not valid")
