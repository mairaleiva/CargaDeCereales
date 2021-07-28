def pedir_calidad():
	"""Solicita al usuario el ingreso de la calidad del cereal representado en un numero y revisa que 
	se encuentre dentro del rango de (0.5 - 1), en caso que no lo este lo vuelve a solicitar hasta
	que se encuentre dentro de dicho rango y lo devuelve"""

	numero = float(input("\nIngrese la calidad del cereal: "))

	while numero < 0.5 or numero > 1:
		print("\nError! El numero esta fuera del rango, vuelva a intentarlo.")
		numero = float(input("Ingrese la calidad del cereal: "))

	return numero