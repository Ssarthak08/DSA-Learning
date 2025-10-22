from abc import ABC, abstractclassmethod


class vehicle(ABC):
    def __init__(self, n):
        self.no_of_types = n

    @abstractclassmethod
    def start(self):
        pass

    def pause(self):
        print("pause")


class Bike(vehicle):
    def __init__(self, types, color):
        super().__init__(types)
        self.color = color

    def start(self):
        print("start with kick")


# class scooty(vehicle):
#     def __init__(self,types,n):
#         super().__init__(types)
#         self.no_of_tyres = 2
#         self.no_of_gears = n
#
#     def start(self):
#         print("Self start")
#
#
# class car(vehicle):
#     def __init__(self):
#         self.no_of_tyres = 4
#
#     def start(self):
#         print("start with keys")

# abstract method denies permission to make objects of a particular class
# and to make any class abstract it should have abstract method too and ABC in its class definition
bike = Bike("G-wagon", "black")
bike.start()  # over here start is coming from bike, not from vehicle even though we have super imposed it
bike.pause()
