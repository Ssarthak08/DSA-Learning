from abc import ABC, abstractclassmethod


class DiscountCalculator(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def calculate_discount(self):
        pass

    def discount(self):
        pass


class FlatDiscount(DiscountCalculator):
    def __init__(self, total_order):
        super().__init__()
        self.order_value = total_order

    def discount_1(self):
        value = self.order_value - 20
        print(f"total amount to be paid after discount {value}")
        print("thank you ")


class PercentageDiscount(DiscountCalculator):
    def __init__(self, total__order):
        super().__init__()
        self.order = total__order

    def discount_2(self):
        value = self.order * 0.10
        print(f"total amount to be paid after discount {value}")
        print("thank you ")




