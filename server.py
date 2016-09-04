import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return request.values.get('data', '')
    else:
        return 'Hello World!'

app.debug = True
app.run(host='0.0.0.0', port=int(os.environ['PORT']))