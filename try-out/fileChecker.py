import os
import json
from dbtests.database import Database

# Print current working directory
print("Current Working Directory:", os.getcwd())

# List files in the current directory
print("Files in the Directory:", os.listdir(os.getcwd()))

# Use the relative path to the file
file_path = "sample_data.json"

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Parse JSON data
        print(data)
else:
    print(f"File {file_path} does not exist.")
