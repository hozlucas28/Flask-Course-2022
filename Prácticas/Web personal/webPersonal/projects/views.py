from flask import render_template, Blueprint
from webPersonal.projects.models import PROJECTS

projectsBP = Blueprint("projects", __name__)

# Página - Proyecto
@projectsBP.route("/projects")
def projects():
    return render_template("./projects/projects.html", projects=PROJECTS)
