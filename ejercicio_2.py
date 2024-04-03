#2.	Calcular el salario de un grupo de n trabajadores dada la cantidad de horas trabajadas y la tarifa por hora para cada uno.

trabajadores = int(input("Ingrese la cantidad de trabajadores: "))

secuencia = 1
total = 0

while secuencia <= trabajadores:
    horastrabajadas = float(input(f"Digite las horas trbajadas por el empleado {secuencia}: "))
    
    tarifahora = float(input(f"Digite la tarifa por hora para el empleado {secuencia}: "))
    
    salario = horastrabajadas * tarifahora
    
    total += salario
    
    secuencia += 1
    
print(f"El salario total del grupo de trabajadores es: {total}")


    
