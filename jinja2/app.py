from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  titulo="Ciudades"
  lista=["Madrid","Londres","New York","LA","Berlín","Dublín"]
  return render_template("index.html", titulo=titulo, lista=lista)

if __name__ == "__main__":
  app.run(debug=True)
