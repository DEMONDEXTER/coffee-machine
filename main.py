

from menu import MenuItem,Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on=True
while is_on:
    option = menu.get_items()
    choice=input(f"Enter your choice: {option}")
    if choice=="off":
        is_on=False
    elif choice=="on":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry, you don't have enough money!")
        else:
            is_on = False


