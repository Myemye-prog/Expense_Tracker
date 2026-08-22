# 💰 Expense Tracker

A simple **console-based Expense Tracker application built using Python**.

This project is created to practice Python concepts such as:

* Functions
* Lists
* Dictionaries
* `if-else`
* `for` loops
* Exception handling
* JSON file handling
* Menu-driven programs

**Repository:** `Myemye-prog`
**Author:** Dipak

---

# 📌 Project Overview

The Expense Tracker allows the user to manage their expenses from the terminal.

The user can:

1. Add an expense
2. View all expenses
3. Delete an expense
4. Calculate total spending
5. Find the highest expense
6. Find the lowest expense
7. Filter expenses by category
8. Save expenses to a JSON file
9. Load expenses from a JSON file
10. Exit the application

---

# 📂 Data Structure

The project uses a **list of dictionaries**.

```python
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
    }
]
```

The outer structure is a **list**.

Each expense inside the list is a **dictionary**.

Each dictionary contains:

```text
amount
category
description
```

---

# 🔄 Main Program Execution Flow

When the program starts:

```text
Start
  ↓
Create empty expense list
  ↓
Display Expense Tracker menu
  ↓
Ask user for choice
  ↓
Check choice
  ↓
┌─────────────────────────────────┐
│ 1 → add_expense()                │
│ 2 → view_expenses()              │
│ 3 → delete_expense()             │
│ 4 → total_spending()             │
│ 5 → highest_expense()            │
│ 6 → lowest_expense()             │
│ 7 → filter_category()            │
│ 8 → save_data()                  │
│ 9 → load_data()                  │
│10 → Exit                         │
└─────────────────────────────────┘
  ↓
After function finishes
  ↓
Show menu again
  ↓
Ask for another choice
  ↓
Continue until user chooses 10
  ↓
End
```

---

# 1️⃣ `add_expense()`

## Purpose

This function adds a new expense to the `expense` list.

## Execution Flow

```text
User selects 1
      ↓
add_expense()
      ↓
Ask for amount
      ↓
Convert input to integer
      ↓
Is amount valid?
    ↓           ↓
   NO          YES
    ↓            ↓
ValueError    Is amount > 0?
    ↓          ↓        ↓
Print error   NO       YES
               ↓         ↓
          Print error   Ask category
                         ↓
                    Ask description
                         ↓
                  Create dictionary
                         ↓
                 Add to expense list
                         ↓
                       Return
```

## Important Code

```python
expense.append({
    "amount": amt,
    "category": ctg,
    "description": descp
})
```

---

# 2️⃣ `view_expenses()`

## Purpose

Displays all expenses stored in the list.

## Execution Flow

```text
User selects 2
      ↓
view_expenses()
      ↓
Is expense list empty?
    ↓           ↓
   YES          NO
    ↓            ↓
Print "No      Start for loop
expenses"        ↓
    ↓        Get each expense
  return          ↓
              Print amount
                  ↓
              Print category
                  ↓
              Print description
                  ↓
              Next expense
                  ↓
              Loop finishes
                  ↓
                Return
```

## Important Code

```python
for i in expense:
    print("Amount:", i["amount"])
    print("Category:", i["category"])
    print("Description:", i["description"])
```

---

# 3️⃣ `delete_expense()`

## Purpose

Deletes an expense using its list index.

## Execution Flow

```text
User selects 3
      ↓
delete_expense()
      ↓
Ask expense number
      ↓
Convert input to integer
      ↓
Is number valid?
    ↓             ↓
   NO            YES
    ↓              ↓
ValueError     Is number >= 0?
    ↓           ↓          ↓
Print error    NO         YES
                ↓           ↓
          Print error    Delete expense
                              ↓
                         del expense[dlt]
                              ↓
                         Print updated list
                              ↓
                            Return
```

## Example

Suppose:

```python
expense = [
    {"amount": 500, "category": "Food"},
    {"amount": 1000, "category": "Travel"}
]
```

If the user enters:

```text
0
```

Python deletes:

```python
expense[0]
```

The Food expense is removed.

---

# 4️⃣ `total_spending()`

## Purpose

Calculates the total amount spent.

## Execution Flow

```text
User selects 4
      ↓
total_spending()
      ↓
Is expense list empty?
    ↓           ↓
   YES          NO
    ↓            ↓
Print error    total = 0
    ↓            ↓
  return      Start loop
                 ↓
          Get expense amount
                 ↓
          total += amount
                 ↓
            Next expense
                 ↓
            Loop finishes
                 ↓
          Print total amount
                 ↓
               Return
```

## Example

```text
Food       = 500
Travel     = 1000
Shopping   = 200

Total = 1700
```

---

# 5️⃣ `highest_expense()`

## Purpose

Finds the expense with the highest amount.

## Execution Flow

```text
User selects 5
      ↓
highest_expense()
      ↓
Is expense list empty?
    ↓           ↓
   YES          NO
    ↓            ↓
Print error    highest = 0
    ↓            ↓
  return      Start loop
                 ↓
        Is current amount
        greater than highest?
             ↓          ↓
            YES         NO
             ↓           ↓
       Update highest  Continue
             ↓
          Next expense
             ↓
         Loop finishes
             ↓
       Print highest
             ↓
           Return
```

## Example

```text
500
1000
200
```

Comparison:

```text
highest = 0
500  > 0    → highest = 500
1000 > 500  → highest = 1000
200  > 1000 → No
```

Final result:

```text
Highest expense is 1000
```

---

# 6️⃣ `lowest_expense()`

## Purpose

Finds the expense with the lowest amount.

## Execution Flow

```text
User selects 6
      ↓
lowest_expense()
      ↓
Is expense list empty?
    ↓           ↓
   YES          NO
    ↓            ↓
Print error    lowest =
    ↓          first expense amount
  return          ↓
              Start loop
                  ↓
          Is current amount
          smaller than lowest?
              ↓          ↓
             YES         NO
              ↓           ↓
        Update lowest   Continue
              ↓
          Next expense
              ↓
          Loop finishes
              ↓
         Print lowest
              ↓
            Return
```

## Why use the first expense?

The code uses:

```python
lowest = expense[0]["amount"]
```

This gives us an actual expense amount to use as the starting value.

---

# 7️⃣ `filter_category()`

## Purpose

Searches for expenses belonging to a specific category.

## Execution Flow

```text
User selects 7
      ↓
filter_category()
      ↓
Ask user for category
      ↓
Is input empty?
    ↓           ↓
   YES          NO
    ↓            ↓
Print error    found = False
    ↓            ↓
  return      Start loop
                 ↓
          Check category
                 ↓
          Does category match?
             ↓          ↓
            YES         NO
             ↓           ↓
        found=True     Continue
             ↓
       Print expense
             ↓
        Next expense
             ↓
        Loop finishes
             ↓
       Is found False?
          ↓        ↓
         YES       NO
          ↓         ↓
    Print "No      Nothing
    expenses"      more
          ↓
        Return
```

## Important Part

```python
found = False
```

At the beginning, we assume that no matching expense exists.

If a match is found:

```python
found = True
```

After the loop:

```python
if not found:
    print("No expenses found for this category.")
```

This is important because we should print "not found" **after checking all expenses**, not inside the loop.

---

# 8️⃣ `save_data()`

## Purpose

Saves the current expenses into a JSON file.

## Execution Flow

save_data()
    ↓
open expense.json
    ↓
Can Python write?
   ↓          ↓
 YES          NO
  ↓            ↓
save data   PermissionError

## Important Code

```python
with open("expense.json", "w") as f:
    json.dump(expense, f)
```

The file created is:

```text
expense.json
```

---

# 9️⃣ `load_data()`

## Purpose

Loads previously saved expenses from the JSON file.

## Execution Flow

load_data()
    │
    ▼
Open expense.json
    │
    ├── File doesn't exist
    │       ↓
    │   FileNotFoundError
    │
    ├── No permission
    │       ↓
    │   PermissionError
    │
    └── File opens
            ↓
        json.load()
            │
            ├── Invalid JSON
            │       ↓
            │   JSONDecodeError
            │
            └── Valid JSON
                    ↓
              expense = data

If the JSON file contains invalid data:

```text
JSONDecodeError
      ↓
Print invalid data message
```

## Important Code

```python
global expense

with open("expense.json", "r") as f:
    expense = json.load(f)
```

`global expense` allows the function to update the global `expense` list.

---

# 🔟 Main Menu Execution Flow

The main program uses an infinite `while` loop.

```python
while True:
```

The flow is:

```text
Start
  ↓
Display menu
  ↓
Ask user choice
  ↓
choice == "1"?
  ↓
Yes → add_expense()
  ↓
Return to menu

choice == "2"?
  ↓
Yes → view_expenses()
  ↓
Return to menu

choice == "3"?
  ↓
Yes → delete_expense()
  ↓
Return to menu

...
  ↓
choice == "10"?
  ↓
Yes
  ↓
Print goodbye message
  ↓
break
  ↓
Program ends
```

---

# 🧩 Complete Program Flow

The complete application works like this:

```text
                    START
                      ↓
             Create expense = []
                      ↓
                Display Menu
                      ↓
              Get User Choice
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
      Choice                      Choice
        1-9                         10
        ↓                           ↓
    Call Function                  Exit
        ↓                           ↓
 Function Performs Task            END
        ↓
    Function Returns
        ↓
    Display Menu Again
        ↓
    Get User Choice
        ↓
      Repeat
```

---

# 📁 Project Structure

```text
Myemye-prog/
│
└── Expense Tracker/
    │
    ├── main.py
    ├── expense.json
    └── README.md
```

> Adjust the folder name above if your actual GitHub folder has a different name.

---

# 🛠️ Technologies Used

* Python 3
* JSON
* Built-in `json` module

No external packages are required.

---

# ▶️ How to Run

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Go to the project folder:

```bash
cd Myemye-prog
```

Run the program:

```bash
python main.py
```

---

# 🎯 Learning Objectives

This project helped me practice:

* Lists
* Dictionaries
* Functions
* Function calls
* `if`, `elif`, `else`
* `for` loops
* `while` loops
* `return`
* `try-except`
* `ValueError`
* `IndexError`
* JSON
* File handling
* `json.dump()`
* `json.load()`
* Menu-driven programs
* Searching and filtering
* Basic problem-solving

---

# 🚀 Future Improvements

Some features that can be added later:

* Edit/update expense
* Add expense date
* Search by description
* Category-wise total
* Monthly reports
* CSV export
* SQLite database
* Tkinter GUI
* Expense charts using Matplotlib

---

# 👨‍💻 Author

**Dipak**

This project is part of my Python practice and is focused on understanding **functions, collections, file handling, exception handling, JSON, and menu-driven applications**.

---

# ⭐ Conclusion

The Expense Tracker is a beginner-friendly Python project that demonstrates how multiple Python concepts can be combined to create a useful real-world application.

The main goal of this project is not only to create an Expense Tracker, but also to understand **how data moves through each function and how the complete program works from start to finish**.
