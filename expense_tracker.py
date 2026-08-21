expense = [
    {
        "amount": 500,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 1000,
        "category": "Travel",
        "description": "Bus"
    },
    {
        "amount": 200,
        "category": "Shopping",
        "description": "Tshirt"
    }
]



#1. Print the amount of the first expense.
print(expense[0]["amount"])

#2. Print the category of the second expense.
print(expense[1]["category"])

#3. Print the description of the third expense.
print(expense[2]["description"])

#4. Use a for loop to print all three dictionaries.
for i in expense:
    print(i)

expense.append({
    "amount":400,
    "category":"Drink",
    "description":"Cold Coffee"
})
print(expense[3])
print()

for i in expense:
    print(i)
print()

#Print expenses nicely
for i in expense:
    print("Amount:",i["amount"])
    print("Category:",i["category"])
    print("Description:",i["description"])
    print()

#Total Spending
total=0
for i in expense:
    total+=i["amount"]
print(f"Total spending is {total}")
print()

#Highest Expense
highest=0
for i in expense:
    if i["amount"]>highest:
        highest=i["amount"]
print("Highest expense is ",highest)

#Lowest Expense
lowest=expense[0]["amount"]
for i in expense:
    if i["amount"]<lowest:
        lowest=i["amount"]
print("Lowest expense is ",lowest)


#Category Filter
# search=input("What you are looking for ")
# for i in expense:
#     if i["category"]==search:
#         print("Amount:",i["amount"])
#         print("Category:",i["category"])
#         print("Description:",i["description"])
#         print()

#Delete Expense
# dlt=int(input("Enter expense number to delete: "))
# del expense[dlt]
# print(expense)

#Add Expense
#You actually started this in your earlier practice, so now let's build it properly.
"""
We want the user to enter:
--------------------------
Enter amount: 300
Enter category: Food
Enter description: Dinner

{
    "amount": 300,
    "category": "Food",
    "description": "Dinner"
}
and add it to:
"""
amt=int(input("Enter amount: "))
ctg=input("Enter category: ")
descp=input("Enter description: ")
expense.append({
    "amount":amt,
    "category":ctg,
    "description":descp
})
# for i in expense:
#     print(i["amount"])
#     print(i["category"])
#     print(i["description"])
#     print()

# import json
# with open("expense.json","w") as f:
#     json.dump(expense,f)

# with open("expense.json","r") as f:
#     expense=json.load(f)

print(expense)