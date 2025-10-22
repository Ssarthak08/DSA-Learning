age = int(input("Enter your age"))
if age >= 15:
    print("you can ride")
    if age <= 20:
        print("enjoy a free ride")
    else:
        print("buy a ticket for $250")
else:
    print("not allowed to ride")
print("buy popcorn too")