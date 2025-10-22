class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_nose = 2

    def eat(self):
        print("I can eat a lot")

    def work(self):
        print("I can work")


class male:
    def __init__(self, name):
        self.name_1 = name

    def flirt(self):
        print("I can flirt very well")

    def work(self):
        print("I can code")


class boy(Human, male):
    def sleep(self):
        print("I can sleep")

    def work(self):
        print("I can test ")


boy_1 = boy()
boy_1.flirt()
boy_1.work()  # in conflict order of writing matters
# but in order to call work of a specific class
# male.work(boy_1)
boy_1.work()

