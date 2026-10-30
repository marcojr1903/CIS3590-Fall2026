import json

# a function to save a json document to a file

def save_json(data, filename):
    with open(filename, 'w') as write_file:
        json.dump(data, write_file)
        print(f"File {filename} saved successfully")

# a function to load a json document from a file
# python recieves the data as a dictionary

def read_from_file(data, file_name):
    with open(file_name, 'r') as read_file:
        data = json.load(read_file)
        print(f"File {file_name} loaded successfully")