from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo!!!"

# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True) # Debug es para que se actualicen los cambios en el servidor sin pararlo
