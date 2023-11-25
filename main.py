from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# menu_item = MenuItem()
while not off:
  choice = input(f"What would you like? {menu.get_items()} or report: ")
  if choice == "off":
    off = True 
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      money_machine.process_coins
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink) 


