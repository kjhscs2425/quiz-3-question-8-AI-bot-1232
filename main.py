import json

# read `expenses.json`
with open('expenses.json', 'r') as file:
    expenses = json.load(file)
# get and print total "price" for all expenses at the "pet store"
pet_store_expenses = expenses.get("pet store", [])

# Calculate the total price
total_price = 0
for item in pet_store_expenses:
    total_price += item['price']

# Print the total price
print(total_price)