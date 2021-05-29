from proyecto import obtenerDato
from flask import Flask, render_template, request,url_for,redirect
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        texto = request.form["todo"]
        datos = obtenerDato(texto)
        traduccion = datos[5]
        textosT = datos[6]
        lon = len(traduccion[0])
        return  render_template('tabla.html',texto=texto,jaccard=datos[0],coseno=datos[1],mayorC=datos[2],mayorJ=datos[3],resultado=datos[4],encontradas=traduccion[0],trad1=traduccion[1],trad2=traduccion[2],trad3=traduccion[3],lon=lon,textosT = textosT)
    else:
        return render_template('index.html')

@app.route("/",methods=['GET','POST']) 
def index_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 