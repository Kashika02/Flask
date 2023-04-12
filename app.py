from flask import Flask, render_template
import requests

# app = Flask(__name__)
app = Flask(__name__, template_folder='template')
api_url = "https://dummyjson.com/products"
api_params = {'key': 'value'}

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/api', methods=["GET"])
def api():
    response = requests.get(api_url, params=api_params)
    data = response.json()
    products = data["products"]
    return render_template("products.html",products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
