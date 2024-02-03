from resource import MENU, resources

profit = 0
machine_start = True


# TODO Prompt user by asking “ What would you like? (espresso/latte/cappuccino):"
# TODO Turn off the Coffee Machine by entering “ off ” to the prompt.
def asking():
    global machine_start
    demand = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while demand not in MENU and demand != "off" and demand != "report":
        print("Please enter a valid choice (espresso/latte/cappuccino)")
        demand = input("What would you like? (espresso/latte/cappuccino): ")
    if demand == "off":
        machine_start = False
    if demand == "report":
        print_report()
    return demand


# TODO Print report.
def print_report():
    for x in resources:
        if x == "coffee":
            print(f"{x}: {resources[x]}g")
        elif x == "profit":
            print(f"{x}: ${resources[x]}")
        else:
            print(f"{x}: {resources[x]}ml")


# TODO Check resources sufficient?
def check_resources(prompt_demand):
    is_enough = True
    for x in resources:
        if x in MENU[prompt_demand]["ingredients"]:
            if resources[x] < MENU[prompt_demand]["ingredients"][x]:
                print(f"Sorry there is not enough {x}.")
                is_enough = False
    return is_enough


# TODO Process coins.
def process_coins():
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickels?: ")
    pennies = input("How many pennies?: ")
    while not quarters.isnumeric() or not dimes.isnumeric() or not nickles.isnumeric() or not pennies.isnumeric():
        print("Please enter a valid number.")
        quarters = input("How many quarters?: ")
        dimes = input("How many dimes?: ")
        nickles = input("How many nickels?: ")
        pennies = input("How many pennies?: ")
    total_amount = 0.25 * int(quarters) + 0.1 * int(dimes) + 0.05 * int(nickles) + 0.01 * int(pennies)
    return total_amount


# TODO Check transaction successful?
def check_transaction(prompt_demand):
    cost_demand = MENU[prompt_demand]["cost"]
    coins_inserted = process_coins()
    if coins_inserted < cost_demand:
        print("Sorry there is not enough money. Money refunded")
        return False
    elif coins_inserted >= cost_demand and check_resources(prompt_demand):
        if coins_inserted > cost_demand:
            print(f"Here is ${(coins_inserted - cost_demand):.2f} dollars in change")
        return True


# TODO Make Coffee.
def make_coffee(prompt_demand):
    global profit
    if check_transaction(prompt_demand):
        profit += MENU[prompt_demand]["cost"]
        resources["profit"] = profit
        for x in resources:
            if x in MENU[prompt_demand]["ingredients"]:
                resources[x] = resources[x] - MENU[prompt_demand]["ingredients"][x]
        print(f"Here is your {prompt_demand}. Enjoy!")


while machine_start:
    prompt_demand = asking()
    if prompt_demand != "off" and prompt_demand != "report":
        make_coffee(prompt_demand)
