from flask import Flask

from flask import request

app = Flask(__name__)

@app.route("/operasBas",methods=["GET", "POST"])
def operasBas():

    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        operacion = request.form.get("operacion")

        if operacion == "SUMA":
            return "LA SUMA DE {} + {} ES IGUAL A {}".format(num1,num2,(num1+num2))
        elif operacion == "RESTA":
            return "LA RESTA DE {} - {} ES IGUAL A {}".format(num1,num2,(num1-num2))
        elif operacion == "MULTIPLICACIÓN":
            return "LA MULTIPLICACIÓN DE {} x {} ES IGUAL A {}".format(num1,num2,(num1*num2))
        elif operacion == "DIVISIÓN":
            return "LA DIVISIÓN DE {} / {} ES IGUAL A {}".format(num1,num2,(num1/num2))
        else:
            return "Selecciona una operación"

        # "LA SUMA ES: {}".format(str(int(num1)+int(num2)))
    else:
        return '''
            <form action="/operasBas" method="POST">
                <label>N1: </label>
                <input type="text" name="num1"/>
                <br><br>
                <label>N2: </label>
                <input type="text" name="num2"/>
                <br><br>
                
                <input type="radio" name="operacion" value="SUMA">
                <label>SUMA</label>
                
                <input type="radio" name="operacion" value="RESTA">
                <label>RESTA</label>
                
                <input type="radio" name="operacion" value="MULTIPLICACIÓN">
                <label>MULTIPLICACIÓN</label>
                
                <input type="radio" name="operacion" value="DIVISIÓN">
                <label>DIVISIÓN</label>
                <br><br>
                <input type="submit" value="Calcular"/>
            </form>            
        '''

if __name__ == "__main__":
    app.run(debug=True)