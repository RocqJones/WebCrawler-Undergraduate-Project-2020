import json
from dbtests.database import Database

with open("sample_data.json", 'r') as file:
    data = file.read()

def analyser(fruits, cerials, vegetables, database):
    f_results = {}
    c_results = {}
    v_results = {}

    for f in fruits:
        f_results[f] = data.count(f)

    for c in cerials:
        c_results[c] = data.count(c)

    for v in vegetables:
        v_results[v] = data.count(v)
    
    print(f_results)
    print(c_results)
    print(v_results)

    # json_obj1 = json.dumps(f_results, indent=2)
    # json_obj2 = json.dumps(c_results, indent=2)
    # json_obj3 = json.dumps(v_results, indent=2)

    # with open("db_data/analyzed_data.json", 'a+') as file:
    #     categories = ["Fruits", "Cerials", "Vegetables"]
    #     # for i in categories:
    #     file.write(json_obj1)
    #     file.write(json_obj2)
    #     file.write(json_obj3)

    # convert dic to a list tuple
    f_list = [(k, v) for k, v in f_results.items()]
    c_list = [(k, v) for k, v in c_results.items()]
    v_list = [(k, v) for k, v in v_results.items()]

    # append the tuple indexes to f,c,veg columns and demand columns
    fp_col = []
    fd_col = []
    for i in f_list:
        fp_col.append(i[0])
        fd_col.append(i[1])

    cp_col = []
    cd_col = []
    for j in c_list:
        cp_col.append(j[0])
        cd_col.append(j[1])

    vp_col = []
    vd_col = []
    for k in v_list:
        vp_col.append(k[0])
        vd_col.append(k[1])

    # iterate through the lists and insert to TABLE FRUITS, CERIALS, and VEGETABLES
    for p in fp_col:
        for d in fd_col:
            database.insert(p, d)

    for p in cp_col:
        for d in cd_col:
            database.insert(p, d)

    for p in vp_col:
        for d in vd_col:
            database.insert(p, d)

    print(database.view())

if __name__ == "__main__":
    fruits = ["Passion", "Mangoes", "Pineapples", "Oranges", "Avocado", "Watermelons", "Strawberries", "Bananas", "Pawpaw"]
    cerials = ["Maize", "Rice", "Beans", "Green Gram",  "Sorghum", "Wheat", "Groundnuts"]
    vegetables = ["Irish Potatoes", "Tomatoes", "Cabbages", "Peas", "Capsicums", "Kales", "Spinach", "Onions", "French Beans", "Carrots", "Broccoli", "Chilli", "Lettuce", "Garlic"]

    database = Database("dbtests/products.db")

    analyser(fruits, cerials, vegetables, database)