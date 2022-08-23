from flask import Flask, request, make_response, redirect
from flask import render_template

# Inicialisamos Flask, con el nombre de la aplicacion
app = Flask(__name__)

@app.route("/")
def index():
    # creamos una variable para rastrear la ip del usuario
    user_ip = request.remote_addr
    # se redirige a la salida de /hello
    response = make_response(redirect("/hello"))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route("/hello")
def hello():
    
    user_ipa = request.cookies.get("user_ipp")
    return render_template('hello.html', user_ip=user_ipa)


