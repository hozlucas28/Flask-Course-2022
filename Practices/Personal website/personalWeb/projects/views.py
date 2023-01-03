# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - <MODELO>.query.all() = Recupera todos los registros de la
#                                      tabla 'MODELO'.
#  			  - <DB>.session.commit() = Es obligatorio luego de realizar una
#                                       consulta para que los cambios se efectuen.
#  			  -  request.form.get(<STRING>) = Recupera el contenido del
#                                             campo, enviado por un formulario.
# ------------------------------------------------------------------------- #


from flask import render_template, Blueprint, request, redirect, url_for
from personalWeb import db
from personalWeb.projects.models import Project

projectsBP = Blueprint("projects", __name__)


# ---------------------------------- Páginas --------------------------------- #

# Inicio
@projectsBP.route("/projects")
@projectsBP.route("/projects/index")
def index():
    projects = Project.query.all()
    db.session.commit()
    return render_template("projects/index.html", projects=projects)


# Insertar
@projectsBP.route("/projects/insert")
def insert():
    return render_template("projects/insert.html")


# Actualizar
@projectsBP.route("/projects/update/<int:id>")
def update(id):
    project = Project.query.get_or_404(id)
    return render_template("projects/update.html", project=project)


# ------------------------------- Base de Datos ------------------------------ #

# Insertar registro
@projectsBP.route("/projects/insert", methods=["POST"])
def insertDB():
    title = request.form.get("title")
    description = request.form.get("description")
    project = Project(title, description)
    db.session.add(project)
    db.session.commit()

    return redirect(url_for("projects.index"))


# Eliminar registro
@projectsBP.route("/projects/delete/<int:id>")
def deleteDB(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()

    return redirect(url_for("projects.index"))


# Actualizar registro
@projectsBP.route("/projects/update/<int:id>", methods=["POST"])
def updateDB(id):
    project = Project.query.get_or_404(id)
    project.title = request.form.get("title")
    project.description = request.form.get("description")
    db.session.add(project)
    db.session.commit()

    return redirect(url_for("projects.index"))
