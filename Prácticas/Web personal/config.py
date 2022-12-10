# ------------------------------------------------------------------------- #
# APUNTES:
# 		   XXX.
#
#
# IMPORTANTE:
#  			  - SQLALCHEMY_DATABASE_URI = Define la URL para conectarse a la
#                                         base de datos.
# ------------------------------------------------------------------------- #

# Base
class Config:
    DEBUG = True
    TESTING = True

    # Base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:289137tx@localhost:3306/webpersonal"


# Producción
class ProductionConfig(Config):
    DEBUG = False


# Desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
