import logging
from flask import Flask, request, jsonify, redirect, render_template

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # the next line is required for Transfer-Encoding support in the request
    request.environ['wsgi.input_terminated'] = True
    return render_template("index.html", 
                            headers=request.headers,
                            body=request.stream.read())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

