# skips whatever is written down below of continue all statements
count = 0
while count <=5:   # condition gets true we enter the loop
    print(count)
    count = count + 1
    if count == 5:
        continue
    print("HEY")
    print("BYE")
print("This statement is out of loop ")