import json

with open("sample_data.json", 'r') as file:
    data = file.read()
    # print(data)

fruits = ["Passion", "Mangoes Local", "Pineapples", "Oranges", "Avocado", "Watermelons", "Strawberries", "Bananas", "Pears", "Papaws"]

results = {}

for f in fruits:
    results[f] = data.count(f)

print(results)