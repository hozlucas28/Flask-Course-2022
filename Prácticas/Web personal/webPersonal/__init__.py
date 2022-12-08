from flask import Flask
from webPersonal.views import baseBP
from webPersonal.projects.views import projectsBP

app = Flask(__name__)
app.register_blueprint(baseBP)  # Registra el 'blue print' del módulo de vistas.
app.register_blueprint(projectsBP)  # Registra el 'blue print' del módulo de vistas.
