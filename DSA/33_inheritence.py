class Human:
    def __init__(self, num_heart):  # attributes
        self.num_eyes = 2
        self.num_nose = 1
        self.heart = num_heart

    def eat(self):  # methods
        print("I can eat")

    def work(self):
        print("I can work")


class male(Human):  # derived class can have methods of its own too
    def __init__(self, name, hear_t):  # after defining this in my sub class I can't access the attributes of main class but methods can be, so to do it
        super().__init__(hear_t)  # ager uper waley se copy ker rhey ho attribute toh apney mei bhi jga bdao na
        self.name_male = name

    def flirt(self):
        print("We can flirt")
        print(f"Hey your name is {self.name_male}")

    def work(self):
        super().work()  # using both the features, work() gives us access to both methods and attributes of parent class
        print("I can work a lot")


male_1 = male("sarthak", "1")  # Object creation
# male_1.work()
# male_1.eat()
# male_1.flirt()
# male_1.work()  # we have over ridden the method
# print(male_1.num_eyes)
male_2 = male("aviral", "2")

# print(male_1.num_nose)
# print(male_2.num_nose)
# print(male_2.heart)
male_2.flirt()
male_2.name_male
