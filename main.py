from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
#menuitem = MenuItem()

print(coffee_maker.is_resource_sufficient(drink=menu.find_drink("latte")))
machine = "on"
while machine == "on":
    selection = input(f"What would you like? {menu.get_items()}: ")
    if selection == "off":
        machine = "off"
        break
    if selection == "report":
        coffee_maker.report()
    if selection == "resources":
        for resource in coffee_maker.resources:
            if resource == "coffee":
                print(f"{resource}: {coffee_maker.resources[resource]} g")
            else:
                print(f"{resource}: {coffee_maker.resources[resource]} ml")

    selection_verified = menu.find_drink(selection)


    if selection_verified is not None:
        can_make = coffee_maker.is_resource_sufficient(drink=menu.find_drink(selection))
        #menuitem.cost = menu.__init__()
        drink_object = menu.find_drink(selection)

        payment = money_machine.make_payment(drink_object.cost)
        if can_make and payment:
            coffee_maker.make_coffee(menu.find_drink(selection))
   #coffee_maker.is_resource_sufficient("latte")
