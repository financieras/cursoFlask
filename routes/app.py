from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello World!"

@app.route("/hola")
def hola():
  return"<h1>Hola</h1>"

@app.route("/user/<string:user>")
def user(user):
  return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
  return "El número es: "+str(n)

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
  return "ID: {}<br>Nombre de usuario: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
  return "La suma de {} y {} es {}.".format(n1,n2,n1+n2)

@app.route("/default/")
@app.route("/default/<string:dft>")
def dft(dft="Cantabria"):
  return "El valor por defecto es " + dft

if __name__ == "__main__":
  #app.run(debug=True, port=3000, host="0.0.0.0")
  app.run(debug=True)
