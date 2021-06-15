from genera import generaPrimos
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  n=100000
  # https://www.w3schools.com/python/ref_string_format.asp
  titulo="Números primos hasta " + '{:,}'.format(n).replace(',', '.')
  return render_template("index.html", titulo=titulo, lista=generaPrimos(n))

if __name__ == "__main__":
  app.run(debug=True)
