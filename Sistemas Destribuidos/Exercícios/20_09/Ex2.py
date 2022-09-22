from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/soma/<int:num1>/<int:num2>', methods=['GET'])
def soma(num1, num2):
  total = num1 + num2
  return jsonify({"soma": total})

@app.route('/sub/<int:num1>/<int:num2>', methods=['GET'])
def sub(num1, num2):
  total = num1 - num2
  return jsonify({"Suabtração": total})

@app.route('/mult/<int:num1>/<int:num2>', methods=['GET'])
def mult(num1, num2):
  total = num1 * num2
  return jsonify({"Multiplicação": total})

@app.route('/div/<int:num1>/<int:num2>', methods=['GET'])
def div(num1, num2):
  total = num1 / num2
  return jsonify({"Divisão": total})

app.run(host='0.0.0.0', port=5000)