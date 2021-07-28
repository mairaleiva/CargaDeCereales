def pide_positivo():
    """Solicita al usuario el ingreso de un número. El valor ingresado debe ser positivo, en caso que no lo sea
    lo vuelve a solicitar hasta que lo sea y lo devuelve."""

    numero = int(input("Ingrese un número, de valor positivo: "))

    while numero <= 0:
        print("\n¡Error! El número ingresado no es positivo. Intente nuevamente")
        numero = int(input("Ingrese un número, de valor positivo: "))
    return numero
