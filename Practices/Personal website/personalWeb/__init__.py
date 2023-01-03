# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - app.config.from_object() = Me permite acudir a una clase para
#                                          definir la configuración de mi
#                                          aplicación Flask.
#  			  - SQLAlchemy() = Inicializa la base de datos.
# ------------------------------------------------------------------------- #


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creación y configuración de la aplicación Flask.
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")


# Inicialización - DB.
db = SQLAlchemy(app)


# Registro de Blueprints
from personalWeb.views import baseBP
from personalWeb.projects.views import projectsBP

app.register_blueprint(baseBP)
app.register_blueprint(projectsBP)


# Ejecutar todas las consultas
with app.app_context():
    db.create_all()
