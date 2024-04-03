#1.	Desarrollar un programa que pida una clave de acceso y deje entrar hasta que sea tecleada la clave correcta. Cada vez que se ingrese una clave incorrecta deberá aparecer el mensaje “Siga intentando”

contraseña = 0

contraseña = int(input("Digite la clave numerica: "))

while contraseña != 12345:
    print("Siga intentando")
    contraseña = int(input("Digite la clave numerica: "))
    if contraseña == 12345:
        break
    
print("Contraseña valida")