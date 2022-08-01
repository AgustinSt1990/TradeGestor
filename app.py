from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template('index.html')

@app.get("/example")
def index():
    return render_template('example.html')

@app.get("/example-p2")
def index():
    return render_template('example-p2.html')


if __name__ == '__main__':
    app.run(debug=True)
