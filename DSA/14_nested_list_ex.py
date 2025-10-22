list_1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]  # 3,2
index_1 = input("Enter the index you want to change")
row_number = int(index_1[0])
column_number = int(index_1[1])
list_1[row_number-1][column_number-1] = 0
print(list_1[0])
print(list_1[1])
print(list_1[2])