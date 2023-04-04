from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink = Menu()
item = MenuItem('name', 'water', 'milk', 'coffee','cost')
make_coffee = CoffeeMaker()
money = MoneyMachine()

turned_on = True


while turned_on:
    choice = input(f"What would you like? {drink.get_items()}: ")

    if choice == "off":
        turned_on = False
    elif choice == "report":
        make_coffee.report()
        money.report()
    else:
        chosen_drink = drink.find_drink(choice)
        if make_coffee.is_resource_sufficient(chosen_drink) and money.make_payment(chosen_drink.cost):
            make_coffee.make_coffee(chosen_drink)



