Python Dictionary vs JSON
-------------------------
Python
------
expense = {
    "amount": 500,
    "category": "Food",
    "description": "Lunch"
}
JSON
----
{
    "amount": 500,
    "category": "Food",
    "description": "Lunch"
}

They look almost identical.
---------------------------
But there is an important difference:
=====================================
Python dictionary is a Python data structure that exists while your Python program is running.

JSON is a data format that can be stored in a file or sent between applications.

-------------------------------------------
💡 Why do we need JSON in Expense Tracker?|
-------------------------------------------
Currently you have:
-------------------
expense = [
    {
        "amount": 500,
        "category": "Food",
        "description": "Lunch"
    }
]

This exists only while your program is running.
-----------------------------------------------
Imagine:
=========
Run program
     ↓
Add ₹500
     ↓
expense list contains ₹500
     ↓
Close program
     ↓
❌ List disappears

We need permanent storage:
==========================
Run program
     ↓
Add ₹500
     ↓
expense list
     ↓
    Save
     ↓
expenses.json

Then tomorrow:
==============
Start program
     ↓
Read expenses.json
     ↓
Get expenses
     ↓
Continue working

That's why JSON is useful for our Version 1 Python Expense Tracker.

🧠 Your expenses.json file

Open your expenses.json file.

You can manually put this inside it for practice:

[
    {
        "amount": 500,
        "category": "Food",
        "description": "Lunch"
    },
    {
        "amount": 1000,
        "category": "Travel",
        "description": "Bus"
    }
]

Notice something important.
===========================
Your Python variable:

expense

is a list.

Therefore the JSON starts with:

[

and ends with:

]

Inside the list are dictionaries/objects.

So:

Python                         JSON


list                           array
[                              [
    dictionary                    object
    {                             {
       "amount": 500               "amount": 500
    }                             }
]                              ]

For our purposes, the structures look very similar.



Excellent work. 🔥 Your complete Load → Add → Save → View flow is correct.
You have now connected the pieces instead of writing isolated examples.
Your program flow
=================
expense.json
     ↓
json.load()
     ↓
expense list
     ↓
Display existing expenses
     ↓
User enters new expense
     ↓
expense.append()
     ↓
Updated expense list
     ↓
json.dump()
     ↓
expense.json
     ↓
Display updated expenses