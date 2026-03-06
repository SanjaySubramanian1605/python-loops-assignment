import json

data = [
  {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
  {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": True}
]

with open("inventory.json", "w") as f:
  json.dump(data, f, indent=4)

# Task 1
with open("inventory.json", "r") as f:
    inventory = json.load(f)

print("Total number of books:", len(inventory))

# Task 2
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}
inventory.append(new_book)
with open("inventory.json", "w") as f:
    json.dump(inventory, f, indent=4)

# Task 3
with open("inventory.json",'r') as f:
   inventory = json.load(f)
   for book in inventory:
       print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")

  