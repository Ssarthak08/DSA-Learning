from abc import ABC, abstractclassmethod


# Abstract class
class DiscountCalculator(ABC):
    @abstractclassmethod
    def calculate_discount(self, order_amount):
        pass


# FlatDiscount class
class FlatDiscount(DiscountCalculator):
    def calculate_discount(self, order_amount):

# PercentageDiscount class
class PercentageDiscount(DiscountCalculator):
    def calculate_discount(self, order_amount):
        if order_amount > 200:
            return order_amount * 0.10  # 10% discount
        return 0  # No discount


customer_1 = FlatDiscount()
customer_1.calculate_discount(150)
