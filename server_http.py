import sys
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return request.values.get('data', '')
    else:
        return 'Hello World!'

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
app.run(host='0.0.0.0', port=port)