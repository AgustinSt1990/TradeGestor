from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """

    # Since this is a website with front-end, we don't need to send the usage instructions
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
