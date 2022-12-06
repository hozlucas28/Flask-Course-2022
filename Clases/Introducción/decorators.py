# ------------------------------------------------------------------------- #
# APUNTES:
# 		   El decorador se aplica a la función ubicada debajo de su llamado.
#          Además el mismo la recibe como argumento.
#
#
# IMPORTANTE:
#  			  - @<NOMBRE DEL DECORADOR> = Llama al decorador.
# ------------------------------------------------------------------------- #

# Decorador
def decorator(function):
    def decorate(*args):
        print("Inicia la ejecución de la función: ", function.__name__)
        function(*args)
        print("Termina la ejecución de la función: ", function.__name__)

    return decorate


@decorator  # Llamado del decorador.
def hi(name):  # Función decorada.
    print(f"¡Hola {name}!")


def add(a, b):  # Función sin decorar.
    print(f"• La suma es: {a + b}")


# Llamados
hi("Lucas")
add(10, 20)
