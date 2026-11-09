from flask import Flask, request
from sympy import isprime
app = Flask(__name__)
@app.route('/alkuluku')
def summa():
    args = request.args
    luku1 = float(args.get("alkuluku"))
    vastaus = isprime(luku1)
    vastaus = {
        "Number" : luku1,
        "isprime" : vastaus
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)