import json

def get_data():

    with open('./api/student_data.json', 'r') as file:
        data = json.load(file)
    return data