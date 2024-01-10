from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
is_on = True

print(coffeeMaker.report())
print(moneyMachine.report())

while is_on:
    options = menu.get_items()
    choice = input(f"What's would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
