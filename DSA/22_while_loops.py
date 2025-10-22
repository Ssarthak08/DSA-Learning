number = int(input("Enter the number : "))
while number != 1:  # jab tak yeh condition false nhi ho jati tab tak else per nhi jayega
    print(number)
    print("good boy")
    number = int(input("Enter the number : "))
else:
    print("this is the else block")
print("this is out of loop ")

# but if you forcibly terminate the while block with break etc then the else block will not work because it's a part
# of while loop only
# in this type of loop firstly the condition is checked
