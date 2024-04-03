#3.	Una planta que fabrica perfiles de hierro posee un lote de n piezas. Desarrollar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida en el rango de 1,20 y 1,30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

piezasaptas = 0
piezasprocesadas = 0 

piezastotales = int(input("Digite la cantidad de piezas a procesar: "))

while piezasprocesadas < piezastotales:
    longitud = float(input("Ingrese la longitud de la pieza {}: ".format(piezasprocesadas + 1)))
    
    if longitud >= 1.20 and longitud <= 1.30:
     piezasaptas += 1

    piezasprocesadas += 1

print("Cantidad de piezas aptas:", piezasaptas)
    

