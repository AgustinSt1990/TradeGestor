from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template('index.html')

# @app.get("/example")
# def example():
#     return render_template('example.html')

# @app.get("/example2")
# def example2():
#     return render_template('example2.html')


if __name__ == '__main__':
    app.run(debug=True)
