from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/alkuluku/<int:number>')
def check_prime(number):

    is_prime = True

    if number < 2:
        is_prime = False

    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    response = {
        "Number": number,
        "isPrime": is_prime
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3000)
