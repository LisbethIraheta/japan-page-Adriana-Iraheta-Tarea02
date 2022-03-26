from flask import Blueprint

messages = Blueprint("messages", __name__)

@messages.route("/messages")
def main():
    return "Funciona la dirección de los mensajes"