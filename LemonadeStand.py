def greetcustomer():
    print("Welcome to the Lemonade Stand")
    print("Fresh Lemonade Made just for you.")

greetcustomer()

price_per_cup = float(input("Enter the price per cup in dollars: "))
cups_sold = int(input("Enter the amount of cups sold: "))

def calculatetotal(price, cups):
    total = price * cups
    return total

total_cost = calculatetotal(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)

print("Total Cost: ", rounded_total)

amount_paid = float(input("Ask how much did the Customer has paid: "))

def calculate_change(paid, total):
    change = total - paid
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thankyoumessage(cups):
    if cups >= 5:
        return "Wow, Thats a big Number. Thank you for buying." 

    else: return "Thanks for stopping by at the stand."

closing_message = thankyoumessage(cups_sold)

print("")
print("==== LEMONADE STAND RECIEPT ====")
print("Price per Cup:", price_per_cup)
print("Cups Sold:", cups_sold)
print("Total Cost:", total_cost)
print("Amount Paid:", amount_paid)
print("Change due:", rounded_change)
print(closing_message)
print("======================================")