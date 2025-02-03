from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

def is_armstrong(n):
    power = len(str(n))
    return sum(int(digit) ** power for digit in str(n)) == n

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}/math?json")
    return response.json().get("text", "No fun fact found.")

@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    number = request.args.get("number")
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    num = int(number)
    properties = []
    if is_armstrong(num):
        properties.append("armstrong")
    properties.append("odd" if num % 2 else "even")

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(num)),
        "fun_fact": get_fun_fact(num),
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
