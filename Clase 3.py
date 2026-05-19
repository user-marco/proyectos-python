# ==========================================
# Exercises to practice the logic
# ==========================================

# ------------------------------------------
# Problem 1: Stock Alert Calculator
# ------------------------------------------
# Situation: A local shop owner wants to automatically know if a product is running low on stock before they completely run out.
# Objective: Create variables for 'current_stock' and 'minimum_required_stock'. Calculate the difference between them and display a clean message in the console showing either how many units are missing to reach the safety limit or how many units are left over.

current_stock = 3
minimum_required_stock = 10
if current_stock < minimum_required_stock:
    units_requireds = minimum_required_stock - current_stock
    print("¡Alert message! Need " + str(units_requireds) + " units to make the stock healthy")
    
# ------------------------------------------
# Problem 2: Profit Margin Calculator
# ------------------------------------------
# Situation: To show local merchants the value of your software, you need to help them calculate exactly how much money they make on each product they sell.
# Objective: Create three variables: 'item_name', 'cost_price' (buying price), and 'selling_price'. Calculate the profit in Soles and the profit margin percentage. Display a report in the console saying: "The product X leaves a profit of S/. Y per unit, which represents a Z% margin."
# Hint: margin_percentage = ((selling_price - cost_price) / cost_price) * 100

item_name = "Laptop"
cost_price = 2500
selling_price = 3000
profit = selling_price - cost_price
margin_percentage = (profit / cost_price) * 100
print("The product " + item_name + ", leaves a profit of S/." + str(profit) + " per unit, which represents a " + str(margin_percentage) + "% margin.")
# ------------------------------------------
# Problem 3: Cash Register Sales Tracker
# ------------------------------------------
# Situation: A store starts the morning with a specific amount of money in the cash register and makes three consecutive sales of the exact same product.
# Objective: Define variables for 'initial_cash' and 'product_price'. Simulating three separate sales, update the cash register variable step-by-step (adding the product price each time). At the very end, print the final balance showing the total money left in the cash register._ 
initial_cash = 80
product_price = 20
cash_register = initial_cash
cash_register += product_price
cash_register += product_price
cash_register += product_price
print(f"Simuling 3 sales the total money in the caja register is {cash_register} ")

