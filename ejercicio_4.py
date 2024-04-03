#4.	En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además, el programa deberá informar el importe que gasta la empresa en sueldos al personal.

nempleados = int(input("Ingrese la cantidad de empleados de la empresa {}: "))

entre100y300 = 0
mas300 = 0 
total = 0

while nempleados > 0:
    salario = int(input("Digite el salario del empleado: "))
    total += salario
    
    if salario >= 100 and salario <= 300:
        entre100y300 += 1
    
    elif salario > 300:
        mas300 += 1
    
    nempleados -= 1
    
print("El numero de empleados  que cobran entre 100 y 300 es: ", entre100y300)
print("El numero de empleados que cobran mas de 300 es: ", mas300)
print("El total que gasta la empresa en salarios es: ",total)
        
    
