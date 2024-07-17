from menu_and_resources import MENU, resources, US_coins


def price(coffee_type):
    coffee_price = MENU[coffee_type]['cost']
    return coffee_price


def amount_water(coffee_type):
    water_amount = MENU[coffee_type]["ingredients"]["water"]
    return water_amount


def amount_coffee(coffee_type):
    coffee_amount = MENU[coffee_type]["ingredients"]["coffee"]
    return coffee_amount


def amount_milk(coffee_type):
    milk_amount = MENU[coffee_type]["ingredients"]["milk"]
    return milk_amount


def check_resources(machine_coffee, machine_water, machine_milk, coffee_selected):
    if machine_water - MENU[coffee_selected]["ingredients"]["water"] <= 0:
        print("Sorry there is not enough water.")
        enough_resources = False
    elif machine_milk - MENU[coffee_selected]["ingredients"]["milk"] <= 0:
        print("Sorry there is not enough milk.")
        enough_resources = False
    elif machine_coffee - MENU[coffee_selected]["ingredients"]["coffee"] <= 0:
        print("Sorry there is not enough coffee.")
        enough_resources = False
    else:
        enough_resources = True
    return enough_resources


def value_inserted():
    quarters_count = int(input("How many quarters?: "))
    quarters_value = US_coins["quarter"] * quarters_count
    dimes_count = int(input("How many dimes?: "))
    dimes_value = US_coins["dime"] * dimes_count
    nickel_count = int(input("How many nickels?: "))
    nickel_value = US_coins["nickel"] * nickel_count
    pennies_count = int(input("How many pennies?: "))
    pennies_value = US_coins["penny"] * pennies_count
    total_value_inserted = quarters_value + dimes_value + nickel_value + pennies_value
    return total_value_inserted


def is_enough(coffee_type, inserted_amount, money):
    price_of_cup = price(coffee_type)
    if inserted_amount < price_of_cup:
        print(f"Sorry that's not enough money for a cup of {coffee_type}. Money refunded.")
    elif inserted_amount > price_of_cup:
        money += price_of_cup
        change = inserted_amount - price_of_cup
        print(f"Thank You. Your change is ${round(change, 2)}.")
        print(f"Here is your {user_input} ☕. Enjoy!")
        return money


current_water = resources["water"]
current_milk = resources["milk"]
current_coffee = resources["coffee"]
current_money = resources["money"]

machine_on = True
while machine_on:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(f"Water: {current_water}ml\nMilk: {current_milk}ml\nCoffee: {current_coffee}g\nMoney: ${current_money} ")
    elif user_input == "off":
        machine_on = False
    elif user_input == "restock":
        current_water = resources["water"]
        current_milk = resources["milk"]
        current_coffee = resources["coffee"]
        current_money = resources["money"]
        print(f"Water: {current_water}ml\nMilk: {current_milk}ml\nCoffee: {current_coffee}g\nMoney: ${current_money} ")
    elif user_input == "espresso" or user_input == "cappuccino" or user_input == "latte":
        resource_check = check_resources(machine_coffee=current_coffee, machine_water=current_water,
                                         machine_milk=current_milk, coffee_selected=user_input)
        if (current_coffee - MENU[user_input]["ingredients"]["coffee"] > 0 and current_water - MENU[user_input][
            "ingredients"][
            "water"] > 0) and current_milk - MENU[user_input]["ingredients"]["milk"] > 0:
            current_coffee = current_coffee - MENU[user_input]["ingredients"]["coffee"]
            current_water = current_water - MENU[user_input]["ingredients"]["water"]
            current_milk = current_milk - MENU[user_input]["ingredients"]["milk"]
        if resource_check:
            print("Please insert coins.")
            amount_of_money_by_user = value_inserted()
            current_money = is_enough(coffee_type=user_input, inserted_amount=amount_of_money_by_user,
                                      money=current_money)
