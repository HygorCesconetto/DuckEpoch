from flask import Flask, request,Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        res = Response()
        res.headers['X-Content-Type-Options'] = '*'
        return res

from back.api import *

if __name__ == "__main__":
    app.run(port=5000, debug=True)