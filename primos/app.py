from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  titulo="Números primos"
  n=200
  lista=[i for i in range(2,n+1)]
  for i, k in enumerate(lista):
    if i<=int(n**.5):
      for j in lista[i+1:]:
        if j % k == 0:
          lista.remove(j)
  return render_template("index.html", titulo=titulo, lista=lista)

if __name__ == "__main__":
  app.run(debug=True)
