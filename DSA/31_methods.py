class Instructor:
    followers = 0  # by default

    def __init__(self, name, address):
        self.ins_name = name
        self.ins_address = address

    def display(self, subject):
        print("Hey baby")
        print(f"Your name is {self.ins_name} and I teach {subject}")  # self wala will fetch info from created objects

    def update_follower(self, follower_name):
        self.followers = self.followers + 1
        # print(self.followers)


instructor_1 = Instructor("Sarthak", "Chandigarh")
instructor_2 = Instructor("Jiya", "delhi")
# print(instructor_1.ins_name)
# print(instructor_2.ins_name)
# print(instructor_1.followers)
# print(instructor_1.display())
# instructor_1.display("Python")
instructor_2.update_follower("Bobby")
print(instructor_2.followers)