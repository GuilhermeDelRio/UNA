document.write("<h1>Estamos executando o script2.js</h1>")
document.write("Esse script está sendo chamado no HEAD")
console.log('teste')

var teste = 1
document.write("<hr> O valor da variável teste é " + teste + "<hr>")
teste = 'Teste'
document.write("<hr> O valor da variável teste agora é " + teste + "<hr>")

nome = 'Guilherme'
console.log(nome.toUpperCase())

var v1 = 5.25
let v2 = null
const v3 = 'teste'

console.log(typeof(v1))
console.log(typeof(v2))
console.log(typeof(v3))
console.log(typeof(NaN))
console.log(typeof(null))
console.log(typeof + Infinity)
const number = "1"

console.log(number == 1)
console.log(number === 1)

var lista = ['arroz', 'Feijão', 'Carne', 'Macarrão']
var listaUl = document.createElement('ul')

var body = document.getElementsByTagName('body')
body[0].appendChild(listaUl)

for (var i=0;i<lista.length;i++) {
  var liFor = document.createElement('li')
  var textoLi = document.createTextNode(lista[i])
  liFor.appendChild(textoLi);
  listaUl.appendChild(liFor);
}

document.write("A LISTA <b>ACIMA</b> foi criada dinamicante com JS")