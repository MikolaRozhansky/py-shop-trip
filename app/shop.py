from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def is_all_product_in_shop(self, customer: object) -> bool:
        for product in customer.product_cart:
            if product not in self.products:
                return False

        return True

    def total_price(self, customer: object) -> float:
        result = 0
        for product in customer.product_cart:
            result += self.products[product] * customer.product_cart[product]
        return round(result, 2)

    def purchase(self, customer: object) -> None:
        current = datetime.now()
        print(current.strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought:")

        for product, amount in customer.product_cart.items():
            cost = round(self.products[product] * amount, 2)
            print(f"{amount} {product} for {cost} dollars")

        print(f"Total cost is {self.total_price(customer)}")
        print("See you again!\n")
