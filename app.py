from flask import Flask, render_template
import requests

app = Flask(__name__)

def api_calls():
    base_url = 'https://api.freeapi.app/api/v1/kitchen-sink/http-methods/get'
    response = requests.get(url=base_url)
    data = response.json()
    
    if data.get("success") and "data" in data:
        product_data = data["data"]
        return product_data
    else:
        return None

@app.route('/')
def index():
    try:
        product_data = api_calls()
        if product_data:
            method = product_data['method']
            host = product_data['headers']['host']
            return render_template('index.html', method=method, host=host)
        else:
            return render_template('index.html', error="Failed to fetch the data!")
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
