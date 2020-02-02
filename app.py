import os
import sys
from flask import Flask

source = " ".join(sys.argv[1:])

app = Flask(__name__)
port = os.getenv("ASPNETCORE_PORT", "5000")

@app.route('/')
def hello():
    return f'Hello from {source}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)