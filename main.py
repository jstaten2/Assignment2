import data
import sandwich_maker
import cashier

recipes = data.recipes
resources = data.resources

maker = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()

### Run the sandwich machine ###


is_on = True

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Bread: {maker.machine_resources['bread']} slice(s)")
        print(f"Ham: {maker.machine_resources['ham']} slice(s)")
        print(f"Cheese: {maker.machine_resources['cheese']} ounce(s)")

    elif choice in recipes:
        sandwich = recipes[choice]
        if maker.check_resources(sandwich["ingredients"]):
            payment = cashier_instance.process_coins()
            if cashier_instance.transaction_result(payment, sandwich["cost"]):
                maker.make_sandwich(choice, sandwich["ingredients"])

    else:
        print("Invalid option.")