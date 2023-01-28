from flask import Flask

app = Flask(__name__)

@app.route("/user/<string:user>")
def user(user):
    return "Hola, cómo estas " + user
    # http://127.0.0.1:5000/user/citlalli

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)
    # http://127.0.0.1:5000/numero/1

@app.route("/user/<int:id>/<string:name>")
def fun(id,name):
    return "ID: {}, NOMBRE: {}".format(id,name)
    # http://127.0.0.1:5000/user/1/citlalli

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma de {} + {} = {}".format(n1,n2,n1+n2)
    # http://127.0.0.1:5000/suma/2.0/2.0

# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True)