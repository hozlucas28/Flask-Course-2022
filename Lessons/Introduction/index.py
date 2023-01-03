# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Las rutas para acceder a las páginas pueden contener argumentos que
#          modifiquen dinámicamente dicha página de destino.
#
#
# IMPORTANTE:
#  			  - @app.route =  define la ruta para acceder a la página debajo
#                             de dicha instrucción.
#  			  - render_template(<HTML>, <ARGUMENTOS>) =  Renderiza dinámicamente
#                                                        el archivo HTML en base
#                                                        a los argumentos enviados.
# ------------------------------------------------------------------------- #

from flask import Flask, render_template

app = Flask(__name__)

# Objeto - Post
class Post:
    def __init__(self, title, description):
        self.title = title
        self.description = description


# Página - Inicio
@app.route("/")  # Ruta primaria.
@app.route("/index")  # Ruta secundaria.
def index():
    message = "¡Hola Mundo con Flask!"
    return render_template("index.html", message=message)


# Página - Blog
@app.route("/blog")  # Ruta.
def blog():
    firstPost = Post("Primer Posteo", "Descripción de mi primer posteo.")
    secondPost = Post("Segundo Posteo", "Descripción de mi segundo posteo.")
    posts = [firstPost, secondPost]
    return render_template("blog.html", posts=posts)


# Página - Saludar
@app.route("/greet")  # Ruta.
@app.route("/greet/<name>")  # Ruta con argumentos - 1.
@app.route("/greet/<name>/<age>")  # Ruta con argumentos - 1.
def greet(name=None, age=None):
    return render_template("greet.html", name=name, age=age)
