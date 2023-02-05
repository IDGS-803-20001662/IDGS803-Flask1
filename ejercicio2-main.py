from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/indexCinepolis")
def indexCinepolis():
    return render_template("indexCinepolis.html")

@app.route("/pagocinepolis", methods=["POST"])
def pagocinepolis():
    nombre = request.form.get("txtNombre")
    cantidadCompradores = int(request.form.get("txtCantidad"))
    tarjeta = request.form.get("rbtTarjeta")
    cantidadBoletos = int(request.form.get("txtBoletos"))
    obj = cinepolis()
    pago = obj.definirDescuento(cantidadCompradores, tarjeta, cantidadBoletos)
    if pago == 0:
        pago = "No se pueden comprar más de 7 boletos por persona"

    return render_template("pagocinepolis.html", nombre= nombre, cantidadBoletos = cantidadBoletos, pago=pago, cantidadCompradores = cantidadCompradores)

#CLASES
class cinepolis():
    cantidadCompradores = 0
    tarjeta = "NO"
    cantidadBoletos = 0
    pago = 0
    descuento = 0

    def definirDescuento(self, cantidadCompradores, tarjeta, cantidadBoletos):
        self.cantidadCompradores = cantidadCompradores
        self.tarjeta = tarjeta
        self.cantidadBoletos = cantidadBoletos

        if cantidadBoletos > 5:
            self.descuento = .15
        elif cantidadBoletos > 2 and cantidadBoletos < 6:
            self.descuento = .10
        else:
            self.descuento = 0

        if tarjeta == "SI":
            self.descuento = self.descuento + .10
        
        self.pago = (12 * cantidadBoletos) - ((12 * cantidadBoletos))*self.descuento

        #por persona no se pueden mas de 7 boletos
        if cantidadBoletos > (cantidadCompradores * 7):
            self.pago = 0
        
        return self.pago



# A partir de que lugar se comienza la ejecucion
if __name__ == "__main__":
    app.run(debug=True,port=3000)