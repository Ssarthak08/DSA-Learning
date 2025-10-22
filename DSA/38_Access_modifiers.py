class Student:
    def __init__(self, name, roll_no, age):
        self.name_1 = name  # this is public attribute
        self._roll_no = roll_no  # this is protected attribute
        self.__age_1 = age  # this is private attribute

    def __display(self):
        print(
            f"Hey my name is {self.name_1} from student class and my age is {self.__age_1}")  # directly bhar ni call out ker saktey

    def privatedata(self):
        print(self.__display())

    def get_age(self):
        return self.__age_1


class branch(Student):
    pass


# s1 = Student("Rahul")
# print(s1.name_1)
# s1.display()
b1 = branch("Sarthak", "25", "100")
print(b1.name_1)
print(b1._roll_no)  # because this is a derived class
# print(b1.__age_1)  because this is private
s1 = Student("rahul", "22", "100")
print(s1.privatedata())
print(dir(s1))  # will; show all private and protected attributes
print(s1._Student__age_1)
print(s1._Student__display)