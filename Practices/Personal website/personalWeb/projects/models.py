# ------------------------------------------------------------------------- #
# APUNTES:
# 		   Este archivo define el modelo de la tabla que se creara en la
#          base de datos, en este caso: Proyectos. Además de definir la
#          clase objeto que se podra insertar en la misma.
#
#
#
# IMPORTANTE:
#  			  - XXX.
# ------------------------------------------------------------------------- #

from personalWeb import db


class Project(db.Model):
    # Nombre de la tabla y columnas
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return f"Project: {self.title}"
