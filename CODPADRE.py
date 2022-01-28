#PROYECTO EMPRESA C1 SOFTWARE
#Carlos Joel Sánchez Galán
#Kelly Katherine Sánchez
#Nathaly Solange Panta Vilela
#Adriana Marcela Mora Vera
#AYUDA ADICIONAL// EDINSON HUMBERTO COLLAHUAZO ROMERO


from HELPERS import HelperCarlitos, validar_carlitos2, validar_carlitos,validar_carlitoscedula,validar_carlitosempleado #Invoca la clase que pertenece a otro modulo
from CARGOS import CargosCarlitos
from DEPARTAMENTO import DepartamentoCarlitos
from EMPLEADOS import EmpleadosCarlitos
from HELPERS import validar_carlitos
import os

def cons_datos(cod,indi):
    esp = ""
    if indi == 1:
        for pos in range(0,len(CargosCarlitos.cargos)):
            valcar = CargosCarlitos.cargos[pos]
            if valcar["codigo"] == cod:
                esp = valcar["cargo"]
    elif indi == 2:
        for pos in range(0,len(DepartamentoCarlitos.departamentos)):
            valdep = DepartamentoCarlitos.departamentos[pos]
            if valdep["codigo"] == cod:
                esp = valdep["departamento"]
    return esp
def busca_cargo(codC):
    c = 0
    for posc in range(0,len(CargosCarlitos.cargos)):
        c = CargosCarlitos.cargos[posc]
        if c["codigo"] == codC:
            c = c["cargo"]
            break
    return c
def busca_departamento(codD):
    d = 0
    for posd in range(0,len(DepartamentoCarlitos.departamentos)):
        d = DepartamentoCarlitos.departamentos[posd]
        if d["codigo"] == codD:
            d = d["departamento"]
            break
    return d
def sea_de(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
################################################################################################################################################################################################
                                                #MENU CARGOS
help = HelperCarlitos()
lista = ["1) Cargo","2) Departamento","3) Empleados","4) Salir"] #para cambiar por el DEBER
opcion = ""
while opcion !="4":                                                     #la opcion 4 es porque es la opcion SALIR
    opcion = help.menuCarlitos(lista, "MENU FICHA PERSONAL")            #Funciona con HELPERS ya que es un titulo
    os.system("cls")                                                    #Sirve para borrar y presentar limpio el codigo en pantalla
    if opcion == "1":                                                   #Estos son los Menus-Padre, dentro de estos van a estar minimenus
        opc1 =""
        while opc1 !="3":
            os.system("cls") 
            opc1= help.menuCarlitos(["1)Ingreso","2)Consulta","3)Salir"],"MANTENIMIENTO DE CARGOS")
            os.system("cls")   
            if opc1 == "1":
                print("*"*20, "INGRESO DE CARGO","*"*20)
                intentos=0
                while True:
                    nombre = input("Ingrese nombre de cargo: ")
                    intentos +=1
                    if validar_carlitos (nombre):
                        print("El cargo introducido fue: {}, correcto?".format(nombre))
                        nombrecargo= CargosCarlitos(nombre)
                        cargo=nombrecargo.registro()
                        CargosCarlitos.cargos.append(cargo)
                        input("Datos ingresados correctamente.")
                        break
                    elif intentos >5:
                        nombre=None
                        print("No cumple los parametros")
                        break
                    
            elif opc1 == "2":
                print("*"*20, "LISTADO DE CARGOS","*"*20) 
                print("Codigo", " "*5, "Descripcion")  
                for nombrecargo in CargosCarlitos.cargos:
                    cod = nombrecargo["codigo"]
                    des = nombrecargo["cargo"]
                    print(" " * 2, cod, " " * 8,des)
                input("Presione una tecla para continuar...")
################################################################################################################################################################################################  
                                          #MENU DEPARTAMENTOS
    elif opcion == "2":
        opc1 =""
        while opc1 !="3":
            os.system("cls") 
            opc1= help.menuCarlitos(["1)Ingreso","2)Consulta","3)Salir"],"MANTENIMIENTO DE DEPARTAMENTO")
            os.system("cls")   
            if opc1 == "1":
                print("*"*20, "INGRESO DE DEPARTAMENTO","*"*20)
                intentos=0
                while True:
                    nombre = input("Ingrese nombre de departamento: ")
                    intentos +=1
                    if validar_carlitos2 (nombre):
                        print("El departamento introducido fue: {}, correcto?".format(nombre))
                        nombredepartamento= DepartamentoCarlitos(nombre)
                        departamento=nombredepartamento.registro()
                        DepartamentoCarlitos.departamentos.append(departamento)
                        input("Datos ingresados correctamente.")
                        break
                    elif intentos >5:
                        nombre=None
                        print("No cumple parametros")
                        break
                    
            elif opc1 == "2":
                print("*"*20, "LISTADO DE DEPARTAMENTOS","*"*20) 
                print("Codigo", " "*5, "Descripcion")  
                for nombredepartamento in DepartamentoCarlitos.departamentos:
                    cod = nombredepartamento["codigo"]
                    des = nombredepartamento["departamento"]
                    print(" " * 2, cod, " " * 8,des)
                input("Presione una tecla para continuar...")

################################################################################################################################################################################################
                                                  #MENU EMPLEADOS

    elif opcion == "3":
        if opcion == "3":
            opc1 = ""
            while opc1 != "3":
                os.system("cls")
                opc1 = help.menuCarlitos(["1) Ingreso", "2) Consulta", "3) Salir"], "MANTENIMIENTO DE EMPLEADOS")
                os.system("cls")
                if opc1 == "1":
                    print("*" * 10, "Ingreso de Empleados", "*" * 10)
                    nombree = input("Ingrese el nombre del Empleado (3-20 Caracteres): ")
                    if validar_carlitosempleado(nombree):
                        print("El nombre introducido ha sido {}, correcto?".format(nombree))
                    cedul = input("Ingrese número de cédula (inserte solo 10 digitos): ")
                    if validar_carlitoscedula(cedul):
                        print("Número de cédula registrado correctamente.")
                    carg = int(input("Ingrese código del cargo: "))
                    cargo3 = busca_cargo(carg)
                    while cargo3 == 0:
                        print(" El código del cargo es inexistente, ingrese codigo valido.")
                        carg = int(input("Ingrese código del Cargo: "))
                        cargo3 = busca_departamento(carg)
                    depart = int(input("Ingrese código del Departamento: "))
                    departamento3 = busca_departamento(depart)
                    while departamento3 == 0:
                        print("El código del departamento es inexistente, ingrese codigo valido.")
                        depart = int(input("Ingrese código del Departamento: "))
                        departamento3 = busca_cargo(depart)
                    sueld = input("Ingrese monto de sueldo: $ ")
                    while sea_de (sueld) is False:
                        print("El monto es incorrecto")
                        sueld = input("Ingrese monto de sueldo: $ ")
                    sueld = round(float(sueld), 2)

                    emp = EmpleadosCarlitos(nombree,cedul,carg,depart,sueld)
                    empleado= emp.registro()
                    EmpleadosCarlitos.Empleados.append(empleado)
                    input("Datos ingresados satisfactoriamente, presione una tecla para continuar...")
                elif opc1 == "2":
                    print("*" * 20, "LISTADO DE EMPLEADOS", "*" * 20)
                    print("Codigo", " " * 3, "Nombre", " "*20, "Cedula", " "*15, "Cargo", " "*14, "Departamento", " "*7, "Sueldo")
                    for emp in EmpleadosCarlitos.Empleados:
                        cod = emp["codigo"]
                        des = emp["nombre"]
                        ced= emp["cedula"]
                        car= emp["cargo"]
                        car1= cons_datos(car,1)
                        dep= emp["departamento"]
                        dep1= cons_datos(dep,2)
                        suel= emp["sueldo"]
                        print(" " * 4, cod, " " *(4-len(str(cod))), des, " " * (25-len(str(des))), ced, " " *(21-len(ced)) , car1," " * (20 -len(str(car1))),dep1, " "*(20-len(dep1)), suel)
                    input("Presione una tecla para continuar...")

    elif opcion == "4":
            print("Saliendo del programa...\n")
    print("Hasta luego :) ....")