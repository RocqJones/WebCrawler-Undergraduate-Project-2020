from backend.database import Database
import os

# sqlite database test
database = Database("backend/data/products.db")

database.insert("Jane Turner", "https://web.com")

print(database.view())

database.update(1,"John Doe", "https://web.com")