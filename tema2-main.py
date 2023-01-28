from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo!!! Hi"

@app.route("/hola")
def hola():
    return "<h1>Hola desde holaaaa</h1>"

@app.route("/adios")
def adios():
    return "<h1>Adioooos</h1>"


# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True)