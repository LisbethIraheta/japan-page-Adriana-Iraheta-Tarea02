from flask import Blueprint

home = Blueprint("home", __name__)

@home.route("/")
def main():
    return "Funciona la dirección web"