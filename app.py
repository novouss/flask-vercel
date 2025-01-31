from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
# from api.index import get_data
import pandas as pd

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def data():
    names = request.args.getlist('name')
    with open('student_data.json', 'r') as file:
        data = pd.read_json(file)
    # data = get_data()
    # students = { entry['name']: entry['marks'] for entry in data if entry['name'] in names }
    results = []
    for name in names:
        mark = data[data['name'] == name]
        if not mark.empty:
            results.append(int(mark['marks'].values[0]))
    
    # results = [ value for _, value in students.items() ]
    return jsonify({ "marks": results })

if __name__ == '__main__':
    app.run(debug=True)
    
