# class Instructor:
#     pass
#
#
# instructor_1 = Instructor()  # object creation
# instructor_1.name = "sarthak"  # attributes of the object
# instructor_1.address = "delhi"
# print(instructor_1.name)
#
# instructor_2 = Instructor()
# instructor_2.name = "Payal"  # attributes of the object
# instructor_2.address = "chandigarh"
# print(instructor_2.name)

# -----------------------------------------------------------------------------------------
class Instructor:
    def __init__(self, name, address, ):
        self.ins_name = name  # everytime a new object is created this function will be called. all these are attributes
        self.ins_address = address
        self.followers = 0  # by default, can be updated in the future


instructor_1 = Instructor("sarthak", "chandigarh")
instructor_2 = Instructor("payal", "delhi")
print(instructor_1.ins_name)
print(instructor_2.ins_name)
print(instructor_2.followers)
