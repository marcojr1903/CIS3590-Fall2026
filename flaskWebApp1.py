from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, CIS 3590!"


@app.route('/aboutUs/<string:name>')
def aboutUs(name):
    return (f"My name is {name}. Our course focuses on teaching internship skills and open-source projects.")

@app.route('/pantherID/<int:id>/<string:fName>')
def pantherID(id, fName):
    return (f"<h2>My name is {fName}, and"
            f" my panther ID is {id}.</h2>")

@app.route('/search')
def search():
    keyword = request.args.get('keyword', default = None)
    limit = request.args.get('limit', default = 5, type = int)
    return f"<h2>Search results for {keyword}, limit {limit}.<h2>"
    # try http://127.0.0.1:5050/search?keyword=python&limit=3


@app.route('/api/data')
def data():
    some_data = {
        "status": "success",
        "course": "CIS 3590",
        "students": 43,
        "semester": "Fall 2026",
        "topics": ["API", "open-source", "git", "streamlit"]
    }
    return jsonify(some_data)

if __name__ == '__main__':
    app.run(debug=True, port = 5050)