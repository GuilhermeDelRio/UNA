from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def rota_raiz():
  return('Rota raiz!')
  

@app.route('/sobre', methods=['GET'])
def rota_sobre():
  return('Sobre')

if __name__ == "__main__":
  app.run()
