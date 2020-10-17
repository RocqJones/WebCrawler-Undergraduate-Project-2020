"""
    Admin can control databases by:
        1. Deleting rows.
        2. View rows according to index.
        3. Update db.
    Admin can also control other backend functions before the data is deployed to end user 
"""
from backend.database import Database
import os

database = Database("backend/data/products.db")

def delete_row():
    print(database.view())
    for symbol in "******":
        print(symbol*2)
    entered_id = int(input("Enter row id: "))
    database.delete(entered_id)
    for symbol in "******":
        print(symbol*2)
    print(database.view())

def view_all():
    print(database.view())

def update_db():
    print(database.view())
    for symbol in "******":
        print(symbol*2)
    id_2_update = int(input("Id to update ? "))
    name_update = input("Update name: ")
    link_update = input("Update link: ")
    database.update(id_2_update, name_update, link_update)
    for symbol in "******":
        print(symbol*2)
    print(database.view())

# options here
print("Please select:\n1. Delete.\n2. View all data from db.\n3. Update database")
option = int(input("Enter option: "))

if option == 1:
    delete_row()

elif option == 2:
    view_all()

elif option == 3:
    update_db()