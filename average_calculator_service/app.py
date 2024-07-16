from flask import Flask, request, jsonify
from utils import calculate_prime_average, calculate_fibonacci_average, calculate_even_average, calculate_random_average

app = Flask(__name__)

@app.route('/average/prime', methods=['POST'])
def prime_average():
    data = request.get_json()
    limit = data['limit']
    average = calculate_prime_average(limit)
    return jsonify({"average": average})

@app.route('/average/fibonacci', methods=['POST'])
def fibonacci_average():
    data = request.get_json()
    limit = data['limit']
    average = calculate_fibonacci_average(limit)
    return jsonify({"average": average})

@app.route('/average/even', methods=['POST'])
def even_average():
    data = request.get_json()
    limit = data['limit']
    average = calculate_even_average(limit)
    return jsonify({"average": average})

@app.route('/average/random', methods=['POST'])
def random_average():
    data = request.get_json()
    count = data['count']
    range_min = data['range']['min']
    range_max = data['range']['max']
    average = calculate_random_average(count, range_min, range_max)
    return jsonify({"average": average})

if __name__ == '__main__':
    app.run(debug=True)
