from backend.database import Database
import os

# sqlite database test
database = Database("backend/db_data/products.db")

database.insert("Cowpeas", "12/10/2018", 8)
database.insert("Beans", "1/01/2020", 5)
database.insert("Rice", "12/10/2019", 8)

print(database.view())

# database.update(1,"Maize", "10/07/2018", 12)
# print(database.view())