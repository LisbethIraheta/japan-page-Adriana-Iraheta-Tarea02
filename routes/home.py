from flask import Blueprint, redirect, render_template, request, url_for
from models.mensajes import Messages
from utils.db import db

home = Blueprint("home", __name__)

@home.route("/")
def main():
    return render_template("japan.html")

@home.route("/nuevo", methods=['POST'])
def nuevo():
    #El request nos sirve para poder ver los datos desde la consola
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email =request.form['email']
    message = request.form['message']
    
    nuevo_mensaje = Messages(firstname, lastname, email, message)
    #print(new_contact) --> Comprobar que esta guardando la información 
    db.session.add(nuevo_mensaje)
    db.session.commit()
    return redirect(url_for('home.main'))

@home.route("/messages")
def mensajes():
    messages = Messages.query.all()
    return render_template("mensajes.html", messages = messages)