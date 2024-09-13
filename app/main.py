import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    # print(os.getcwd())

    with open("config.json", "r") as f:
        datas = json.load(f)

    fuel_price = datas["FUEL_PRICE"]

    customer_inst = []
    shop_inst = []

    for customer in datas["customers"]:
        customer_inst.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            )
        )
        )

    for shop in datas["shops"]:
        shop_inst.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]

            )
        )

    for customer in customer_inst:
        print(f"{customer.name} has {customer.money} dollars")

        lowest_spent = 0
        flag = True

        for shop in shop_inst:
            if shop.is_all_product_in_shop(customer):
                money_spent = customer.car.cost_trip(
                    customer, shop, fuel_price
                )
                if flag:
                    lowest_spent = money_spent
                    lowest_shop_inst = shop
                    flag = False
                else:
                    if money_spent < lowest_spent:
                        lowest_spent = money_spent
                        lowest_shop_inst = shop

        if customer.money <= lowest_spent:
            print(
                f"{customer.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            continue

        # print(f"Lowest shop {lowest_shop_inst.name} {lowest_spent}")
        customer.customer_to_shop(lowest_shop_inst)
        lowest_shop_inst.purchase(customer)
        customer.customer_to_home(lowest_spent)
#
# if __name__ == "__main__":
#     shop_trip()
