# retoSemana1
Ciclo 1: Fundamentos de programación
Reto 1
Descripción del problema:

Un ganadero desea comprar 119 animales y sabe de antemano que por 18 que inicialmente compró
pago un total de 9.725.482,00 pesos, por lo cual el ganadero se pregunta cuanto pagará por cada
animal para así considerar la compra de tantos de ellos? . Tome en cuenta como dato valioso que
el distribuidor de animales le descontará un 15% por cada animal debido a una compra tan alta.

Para darle solución al planteamiento, el usuario debe introducir por teclado la cantidades de
animales a comprar, en este caso 119, para así determinar la cantidad de dinero a pagar por esa
cantidad de animales menos el descuento de 15%. Finalmente, desarrollar la función que contenga
la lógica (operaciones aritméticas) de la misma.

Entradas:

Nombre Tipo Descripción
cantidadAnimales Int Cantidad de animales a comprar

Salidas
Tipo de retorno Descripción
Str Cadena de caracteres de la forma " Ud con un descuento
del 15% paga un valor de: " + str(valorTotalActual)

Ejemplos:

CantidadAnimales Valor de retorno
119 Ud con un descuento del 15% paga un valor de: 5465180.58
150 Ud con un descuento del 15% paga un valor de: 6888883.08
205 Ud con un descuento del 15% paga un valor de: 9414806.88

Esqueleto:

def Logica(cantidadAnimales):
 """ Compra de animales por un ganadero
 Parametros:
 --------------
 ventaInicial (float):
 Costo inicial por la compra de 18 animales (por defecto 9725482.00 )
 animalInicial (int):
 Cantidad inicial de animales comprados (por defecto 18)
 Descuento (float):
 Porcentaje de descuento por la compra de mas de 100 animales (por defecto 0.085)
 valorTotalActual (float):
 Calculo del monto a pagar con el descuento
 Retorna:
 ----------
 str: Cadena de caracteres de la forma " Ud con un descuento del 15% paga un valor de: " +
str(valorTotalActual).
"""
