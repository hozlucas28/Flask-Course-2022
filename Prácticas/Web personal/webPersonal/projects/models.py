class Project:
    def __init__(self, title, description):
        self.title = title
        self.description = description


firstProject = Project("Primer Proyecto", "Descripción breve del primer proyecto")
secondProject = Project("Segundo Proyecto", "Descripción breve del segundo proyecto")
thirdProject = Project("Tercer Proyecto", "Descripción breve del tercer proyecto")
PROJECTS = [firstProject, secondProject, thirdProject]
