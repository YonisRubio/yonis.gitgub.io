from flask import Flask, request, make_response, redirect
from flask import render_template

# Inicialisamos Flask, con el nombre de la aplicacion
app = Flask(__name__)

todos = ["Cafe", "Harina", "Pan", "Azucar"]
@app.errorhandler(404)
def not_found(error):
    return f'caracas 364'



@app.route("/")
def index():
    # creamos una variable para rastrear la ip del usuario
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie('user_ip', user_ip)

    return response


@app.route("/hello")
def hello():
    user_ipa = request.cookies.get("user_ip")
    
    contenido = {
        "user_ip": user_ipa,
        "todos": todos}
    return render_template('hello.html',**contenido)


