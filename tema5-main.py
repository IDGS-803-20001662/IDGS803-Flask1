from flask import Flask, render_template
#El render template busca automaticamente el archivo en la carpeta TEMPLATES

app = Flask(__name__)

@app.route("/")
def index():
    nombre = "Juan"
    lista1 = ["Español", "Ingles", "Quimica"]
    return render_template("index.html", nombre = nombre, lista1 = lista1)

@app.route("/usuarios")
def usuarios():
    return render_template("archivo2.html")


# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True)