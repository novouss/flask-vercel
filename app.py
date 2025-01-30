from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from api.index import get_data

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def data():
    names = request.args.getlist('name')
    data = get_data()
    students = { entry['name']: entry['marks'] for entry in data if entry['name'] in names }
    results = [ value for _, value in students.items() ]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)