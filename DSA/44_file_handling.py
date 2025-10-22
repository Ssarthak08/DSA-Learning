# with open("file_1.txt",'r') as f:
#     data=f.read()
#
#     new_data=data.replace("Java", 'Python')
#     print(new_data)
# with open("file_1.txt",'w') as f:
#     f.write(new_data)
with open("file_1.txt","r") as f :
    data=f.read()
    if data.find("learning") != -1:
        print("found")
    else:
        print("not found")
