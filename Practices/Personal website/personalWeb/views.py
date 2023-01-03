# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Los 'blue prints' me permiten modularizar mi proyecto, evitando
#          la importación de app desde el módulo principal.
#
#
# IMPORTANTE:
#  			  - XXX.
# ------------------------------------------------------------------------- #

from flask import render_template, Blueprint

baseBP = Blueprint("base", __name__)

# Página - Inicio
@baseBP.route("/")
@baseBP.route("/home")
def home():
    return render_template("./index.html")


# Página - Portafolio
@baseBP.route("/portfolio")
def portfolio():
    return render_template("./portfolio.html")


# Página - Contacto
@baseBP.route("/contact")
def contact():
    return render_template("./contact.html")
