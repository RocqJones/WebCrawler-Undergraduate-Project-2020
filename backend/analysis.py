import json
from database import Database

with open("db_data/sample_data.json", 'r') as file:
    data = file.read()

def fruits_analyser(fruits, database):
    f_results = {}
    for f in fruits:
        f_results[f] = data.count(f)

    print(f_results)

    # convert dic to a list tuple
    f_list = [(k, v) for k, v in f_results.items()]

    # append the tuple indexes to f,c,veg columns and demand columns
    fp_col = []
    fd_col = []
    for i in f_list:
        fp_col.append(i[0])
        fd_col.append(i[1])

    # iterate through the lists and insert to TABLE FRUITS
    for p in fp_col:
        for d in fd_col:
            database.insert(p, d)

def cerials_analyser(cerials, database):
    c_results = {}
    for c in cerials:
        c_results[c] = data.count(c)

    print(c_results)

    c_list = [(k, v) for k, v in c_results.items()]

    cp_col = []
    cd_col = []
    for j in c_list:
        cp_col.append(j[0])
        cd_col.append(j[1])

    for p in cp_col:
        for d in cd_col:
            database.insert(p, d)

def vegetables_analyser(vegetables, database):
    v_results = {}
    for v in vegetables:
        v_results[v] = data.count(v)
    
    print(v_results)

    v_list = [(k, v) for k, v in v_results.items()]

    vp_col = []
    vd_col = []
    for k in v_list:
        vp_col.append(k[0])
        vd_col.append(k[1])

    for p in vp_col:
        for d in vd_col:
            database.insert(p, d)

if __name__ == "__main__":
    fruits = ["Passion", "Mangoes", "Pineapples", "Oranges", "Avocado", "Watermelons", "Strawberries", "Bananas", "Pawpaw"]
    cerials = ["Maize", "Rice", "Beans", "Green Gram",  "Sorghum", "Wheat", "Groundnuts"]
    vegetables = ["Irish Potatoes", "Tomatoes", "Cabbages", "Peas", "Capsicums", "Kales", "Spinach", "Onions", "French Beans", "Carrots", "Broccoli", "Chilli", "Lettuce", "Garlic"]

    database = Database("db_data/products.db")

    fruits_analyser(fruits, database)
    cerials_analyser(cerials, database)
    vegetables_analyser(vegetables, database)

    print(database.view())