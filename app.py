from flask import Flask, render_template, request, jsonify
import time
import math
import threading

app = Flask(__name__)

# Simulate CPU-intensive task
def calculate_primes(n):
    primes = []
    for num in range(2, n):
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    return primes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-form', methods=['GET'])
def get_form():
    return render_template('get_form.html')

@app.route('/post-form', methods=['GET', 'POST'])
def post_form():
    if request.method == 'POST':
        data = request.form.get('input_data')
        result = calculate_primes(int(data))  # Simulate resource usage
        return jsonify({"message": f"Calculated {len(result)} primes."})
    return render_template('post_form.html')

@app.route('/api/resource-intensive', methods=['POST'])
def resource_intensive():
    data = request.json.get('number')
    n = int(data)
    primes = calculate_primes(n)
    return jsonify({"message": f"Found {len(primes)} primes below {n}."})

@app.route('/api/slow', methods=['GET'])
def slow_request():
    time.sleep(5)  # Simulate a slow operation
    return jsonify({"message": "This was a slow request."})

@app.route('/simulate-multiple-threads', methods=['POST'])
def simulate_threads():
    n = int(request.json.get('threads', 5))
    threads = []
    for _ in range(n):
        thread = threading.Thread(target=calculate_primes, args=(10000,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return jsonify({"message": f"Simulated {n} threads performing resource-intensive tasks."})

if __name__ == "__main__":
    app.run(debug=True)
