from PedirCalidad import pedir_calidad
from PidePositivo import pide_positivo
from PedirCereal import pedir_cereal


def calcular_facturacion(precio_cereal,cotizacion_dolar,cant_cereal,calidad_cereal):

	cant_toneladas = cant_cereal / 1000
	cant_horas = cant_toneladas / 1200
	costo_horas = 500 * cotizacion_dolar * cant_horas
	valor_cereal = precio_cereal * cant_toneladas * calidad_cereal

	facturacion = round(0.002 * valor_cereal + costo_horas,2)

	return facturacion


def main():
	cant_embarques = 0
	facturacion_max = 0
	cant_soja = 0
	cant_girasol = 0
	precio_cereal = 0
	facturacion_total = 0

	print("Introduzca la cotizacion semanal del dolar")
	cotizacion_dolar = pide_positivo()

	print("\nIntroduzca el precio de la tonelada de Soja en pesos")
	precio_soja = pide_positivo()

	print("\nIntroduzca el precio de la tonelada de Girasol en pesos")
	precio_girasol = pide_positivo()

	print("\nIntroduzca '*' para terminar")
	id_buque = input("Introduzca la identificacion del buque: ")

	while id_buque != '*':

		tipo_cereal = pedir_cereal()

		calidad_cereal = pedir_calidad()

		print("\nIntroduzca la cantidad de cereal a despachar en Kg")
		cant_cereal = pide_positivo()

		if tipo_cereal.lower() == 'soja':
			precio_cereal = precio_soja
			cant_soja += cant_cereal

		else:
			precio_cereal = precio_girasol
			cant_girasol += cant_cereal

		facturacion = calcular_facturacion(precio_cereal,cotizacion_dolar,cant_cereal,calidad_cereal)

		print("\nLa facturacion actual de su embarque '{}' es de {}$ ARS".format(id_buque,facturacion))

		facturacion_total += facturacion
		cant_embarques += 1

		if facturacion > facturacion_max:
			facturacion_max = facturacion

		print("\nIntroduzca '*' para terminar")
		id_buque = input("Introduzca la identificacion del buque: ")

	print("""
		Cantidad total de embarques despachados: {}\n
		Cantidad de Girasol despachado: {} Tn\n
		Cantidad de Soja despachada: {} Tn\n
		Facturacion Maxima registrada: {}$ ARS\n
		Facturacion total: {}$ ARS""".format(cant_embarques, cant_girasol / 1000, cant_soja / 1000, facturacion_max, facturacion_total))



main()


