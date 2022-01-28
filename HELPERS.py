class HelperCarlitos:
    def __init__(self):
        pass
    def menuCarlitos (self, opciones,titulo):
        print("*"*20,titulo,"*"*20) #Ayuda a la aparicion de los titulos a lo largo del codigo
        for opcion in opciones:
            print(opcion)
        opc= input ("elija opcion 1...{}: " .format(len(opciones)))
        return opc
    
def validar_carlitos(validar):
    if len(validar)>20:
        print("Ingrese una cantidad menor a 20 caracteres")
    elif len(validar) <1:
        print("Ingrese una cantidad mayor a 1 caracter")
    else: 
        print("Datos ingresados correctamente")
        return True
    
def validar_carlitos2(validar):
    if len(validar)>20:
        print("Ingrese una cantidad menor a 20 caracteres")
    elif len(validar) <5:
        print("Ingrese una cantidad mayor a 5 caracter")
    else: 
        print("Datos ingresados correctamente")
        return True

def validar_carlitosempleado(empl):
    while (len(empl) < 3 or len(empl) > 20):
        print(" Incorrecto, Nuevamente ingrese ")
        empl = input("   Nombre: ")
    return empl
def validar_carlitoscedula(cedula):
    while len(cedula) != 10 or not cedula.isdigit():
        print("Incorrecto, Ingrese cédula de 10 dígitos")
        cedula = input("   CEDULA: ")
    return cedula


