def pedir_cereal():
    """ Solicita al usuario que ingrese el tipo de cereal y verifica que sea ‘Soja’ o ‘Girasol’
          y en caso que no lo sea lo vuelve a solicitar hasta que sea un tipo de cereal valido."""

    tipo_cereal = input("\nTipo de cereal a transportar (Girasol / Soja)\nTipo de Cereal: ")

    while tipo_cereal.lower() != 'soja' and tipo_cereal.lower() != 'girasol':
        tipo_cereal = input("\nOpcion no valida, vuelva a ingresar una opcion: ")

    return tipo_cereal