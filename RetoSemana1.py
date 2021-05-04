ventaInicial = 9725482.00
animalInicial = ventaInicial / 18
descuento = 0.085

cantidadAnimales = int(input('Bienvenido, ingrese la cantidad de animales que desea comprar '))
valorTotalActual = cantidadAnimales * animalInicial

if cantidadAnimales >= 100:
    print('Ud con un descuento del 15% paga un valor de: ', + valorTotalActual*descuento)
else:
    print('Ud sin descuento paga un valor de: ', + valorTotalActual)