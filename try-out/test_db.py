from dbtests.database import Database
import os

# sqlite database test
database = Database("dbtests/products.db")

# database.insert("Cowpeas", 8)
# database.insert("Beans", 5)
with open("sample_data.json", 'r') as file:
    data = file.read()

fruits = ["Passion", "Mangoes Local", "Pineapples", "Oranges", "Avocado", "Watermelons", "Strawberries", "Bananas", "Pears", "Papaws"]

results = {}
for f in fruits:
    results[f] = data.count(f)
print(results)

# convert dic to a list tuple
r_list = [(k, v) for k, v in results.items()] 
print(r_list)

# append the tuple indexes to product column and demand column
p_col = []
d_col = []
for i in r_list:
    p_col.append(i[0])
    d_col.append(i[1])

print(p_col)
print(d_col)

# iterate through the lists and insert to db
for p in p_col:
    for d in d_col:
        database.insert(p, d)

print(database.view())

# database.update(1,"Passion", 12)
# print(database.view())