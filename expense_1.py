import json

# Loads expense.json
with open("expense.json","r") as f:
    expense=json.load(f)

# Prints the existing expenses
for i in expense:
    print(i["amount"])
    print(i["category"])
    print(i["description"])
    print("="*10)

# Adds one new expense
amt=int(input("Enter spent amount: "))
ctg=input("Enter where did spend amount: ")
descp=input("Enter enter what you buy: ")
expense.append({
    "amount":amt,
    "category":ctg,
    "description":descp
})
# Saves the updated list back to expense.json
with open("expense.json","w") as f:
    json.dump(expense,f)
# Prints the updated list
for i in expense:
    print(i["amount"])
    print(i["category"])
    print(i["description"])
    print("="*10)
