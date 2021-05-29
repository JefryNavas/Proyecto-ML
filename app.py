""" from proyecto import obtenerDato """
from flask import Flask, render_template, request,url_for,redirect
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        texto = request.form["todo"]

        return  render_template('tabla.html',texto=texto)
    else:
        return render_template('index.html')

@app.route("/",methods=['GET','POST']) 
def index_func():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 