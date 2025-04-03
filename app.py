from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Azure Terraform!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
