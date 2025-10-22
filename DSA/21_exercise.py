# taking input from the user and entering into list and taking average
height = []
sum = 0
for i in range(0,5):
    height_input = int(input("Enter your height :"))
    height.append(height_input)
print("The entered height are : " + str(height))
for i in height:
    sum = sum + i
sum = sum/5
print("The average of all the heights are :" + str(sum))
