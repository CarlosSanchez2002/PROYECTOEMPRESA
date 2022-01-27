
class Ejercicios:
#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es
#menor. Considerar el caso en que ambos números son iguales.
    def Ejercicio6_1(self):
        x1=int(input("Ingrese un número:"))
        x2=int(input("Ingrese un segundo número:"))
        if x1<x2:
            print("El primer numero es menor al segundo")
        elif x2<x1:
            print("El segundo numero es menor al primero")
        else:
            print("Ambos digitos son iguales") 
        
    def Ejercicio6_2(self):  
# Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si
#es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es 
#sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro
#mensaje.
        dia_sema=input("Ingrese un dia de la semana: ")
        if (dia_sema=="lunes"):
            print("Odio los lune’")
        elif (dia_sema=="viernes") :
            print("Es hora de ir a loquiar")
        elif (dia_sema=="sabado" or "domingo"):
            print("Hay que descansar para la nueva semana")
        else:
            print("De nuevo a esperar una semana :,)")        
    def Ejercicio6_3(self): 
# Escribir un programa que, dado un número entero, muestre su valor absoluto.
#Nota: para los números positivos su valor absoluto es igual al número (el
#valor absoluto de 52 es 52), mientras que, para los negativos, su valor
#absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
        xvnumero=int(input("Inrese un número:"))
        if xvnumero<0:
            xvnumero=xvnumero*-1
        print("el valor absoluto:", xvnumero)
# Solicitar al usuario que ingrese los nombres de dos personas, los cuales se
# almacenarán en dos variables. A continuación, imprimir “coincidencia” si los
# nombres de ambas personas comienzan con la misma letra ó si terminan con
# la misma letra. Si no es así, imprimir “no hay coincidencia”.
    def Ejercicio6_4(self): 
        varnombre1=input("Ingrese un nombre: ")
        varnombre2=input("Ingrese un segundo nombre: ")
        posicion_final_nombre1=len(varnombre1)-1
        posicion_final_nombre2=len(varnombre2)-1
        if varnombre1[0] == varnombre2[0] or varnombre1[posicion_final_nombre1] == varnombre2[posicion_final_nombre2]:
            print("Se encontraron coincidencias")
        else:
            print("No se encontraron coincidencias")
# Crear un programa que permita al usuario elegir un candidato por el cual
# votar. Las posibilidades son: candidato A por el partido rojo, candidato B por
# el partido verde, candidato C por el partido azul. Según el candidato elegido
# (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido
# [color que corresponda al candidato elegido]”. Si el usuario ingresa una
# opción que no corresponde a ninguno de los candidatos disponibles, indicar
# “Opción errónea”.
    def Ejercicio6_5(self): 
        postular_candidato=input("inserte un candidato elegido: ")
        if postular_candidato.upper()=="A":
            print("Usted votó por el partido rojo")
        elif postular_candidato.upper()=="B":
            print("Usted votó por el partido verde")
        elif postular_candidato.upper()=="C":
            print("Usted votó por el partido azul")
        else:
            print("Opción errónea") 
# Escribir un programa que solicite al usuario una letra y, si es una vocal,
# muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un
# carácter. Si ingresa un string de más de un carácter, informarle que no se
# puede procesar el dato. 
    def Ejercicio6_6(self):     
        letras=input("Ingrese unaLetra:")
        if len(letras)!=1:
            print("Solo ingrese una letra")
        else:
            if letras in "aeiou":
                print("Es vocal")        
# Hacer un programa que permita saber si un año es bisiesto. Para que un año
# sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto
# que también sea divisible por 400.       
    def Ejercicio6_6(self):       
        año=int(input("Año:"))
        if año%4 == 0:
            if año%100 != 0 or año%400 == 0:
                print("El año si es bisiesto")
            else:
                print("El año no es bisiesto")
        else:
            print("El año no es bisiesto")      
# Un instituto de enseñanza de inglés necesita un programa que le permita, cada
# día, procesar observaciones sobre las clases de ese día. El instituto dicta
# clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de
# la semana diferente: los lunes se dicta el nivel inicial, los martes el nivel
# intermedio, los miércoles el nivel avanzado, los jueves son para práctica
# hablada y los viernes se dicta inglés para viajeros.
# Se debe comenzar por solicitar al usuario que ingrese la fecha actual en
# formato "día, DD/MM", donde [día] es un día de la semana, DD es el número
# de día y MM es el número de mes. Si el usuario ingresa un día de la semana
# inexistente o una fecha cuyo día supere el número 31 o el mes supere el
# número 12, finalizar el programa indicando que se produjo un error. Debe
# permitirse que ingrese el día de la semana en minúsculas o mayúsculas
# indistintamente. Como precondición se tiene que lo ingresado por el usuario
# tendrá la forma <[alfanumérico], [numérico]/[numérico]>.
# Una vez indicada la fecha, el usuario necesita poder indicar si ese día se
# tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio
# o avanzado, ya que las prácticas habladas y el inglés para viajeros no tienen
# exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos
# aprobaron y cuántos no, y el programa le mostrará el porcentaje de
# aprobados.
# Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar
# el porcentaje de asistencia a clase y el programa le indicará "asistió la 
# Página 21 de 26
# mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la
# mayoría" si no es así.
# Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del
# mes 1 o del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar
# al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en
# $ por cada alumno, para luego imprimir el ingreso total en $.        
    def Ejercicio6_6(self):       
        fechacjsg=input("ingrese una fecha (el formato debe ser  'día,mes DD/MM'): ")
        fechacjsg=fechacjsg.lower()
        diasemana=fechacjsg[0:fechacjsg.find(',')]
        dianro=int(fechacjsg[fechacjsg.find(',')+2:fechacjsg.find('/')])
        mesnro=int(fechacjsg[fechacjsg.find('/')+1:])
        if dianro>31 or mesnro>12:
            print("Ingrese una fecha valida")
        else:
            if diasemana in "lunes,martes,miércoles":
                respuesta=input("¿Se tomaron exámenes? S/N: ")
                if respuesta.lower()=="s":
                    aprobados=int(input("inserte la cantidad de aprobados: "))
                    reprobados=int(input("inserte la cantidad de reprobados: "))
                    print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
            elif diasemana=="jueves":
                asistencia=int(input("Porcentaje de asistencia: "))
                if asistencia>50:
                    print("Asistió la mayoría")
                else:
                    print("No asistió la mayoría")
            elif diasemana=="viernes":
                if dianro==1 and (mesnro==1 or mesnro==7):
                    print("Nuevo ciclo")
                    alumnos=int(input("Cantidad de alumnos: "))
                    arancel=float(input("Arancel: $"))
                    print("Ingreso total: $", alumnos*arancel)
            else:
                print("Fecha incorrecta")
        print("Fin del programa")       
        
        
        
# Leer números enteros de teclado, hasta que el usuario ingrese el 0.
# Finalmente, mostrar la sumatoria de todos los números ingresados.
    def Ejercicio6_7(self): 
        total=0
        número=int(input("Ingrese un número: "))
        while número != 0:
            total+=número
            número=int(input("Ingrese un número: "))        
# Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
    def Ejercicio6_8(self): 
        num_positivos=0
        n=int(input("Ingrese un numero (0 si desea terminar): "))
        while n!=0:
            if n>0:
                num_positivos+=1
            n=int(input("Ingrese un numero (0 si desea terminar): "))
        print("Cantidad de numeros positivos:", num_positivos)        
# Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
# Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0.
# Informar cuál fue el mayor número ingresado.
    def Ejercicio6_9(self): 
        num_mayor=-1
        n=int(input("Ingrese un número positivo:"))
        while n>=0:
            if n>num_mayor:
                num_mayor=n
        n=int(input("Ingrese un número positivo:"))
        print("El numero mayor ingresado:", num_mayor)        
# Leer un número entero positivo desde teclado e imprimir la suma de los
# dígitos que lo componen.
    def Ejercicio6_10(self): 
        sumacjsg=0
        num=int(input("Ingrese un número positivo:"))
        while num!=0:
            digito=num%10
            sumacjsg+=digito
            num=num//10
        print("Suma de los dígitos es:", sumacjsg)        
# Solicitar al usuario que ingrese números enteros positivos y, por cada uno,
# imprimir la suma de los dígitos que lo componen. La condición de corte es
# que se ingrese el número -1. Al finalizar, mostrar cuántos de los números
# ingresados por el usuario fueron números pares.
    def Ejercicio6_11(self): 
        num_pares=0
        n=int(input("Inserte un numero (ingrese -1 si desea terminar el programa): "))
        while n!=-1:
            if n%2 == 0:
                num_pares+=1
            sumacjsg=0
            while n!=0:
                digito=n%10
                sumacjsg+=digito
                n=n//10
            print("La suma de sus dígitos:", sumacjsg)
            n=int(input("Inserte un numero (ingrese -1 si desea terminar el programa):"))
        print("Se ingresaron", num_pares, "números pares")        
# Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir
# listado, 3-finalizar programa. A continuación, el usuario debe poder
# seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle
# del error. El menú se debe volver a mostrar luego de ejecutada cada opción,
# permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto.
# Si elige la opción 3, se interrumpirá la impresión del menú y el programa
# finalizará.
    def Ejercicio6_12(self): 
        while True:
            print("Opción 1 - Comenzar programa")
            print("Opción 2 - Imprimir listado")
            print("Opción 3 - Cinalizar programa")
            opcion=int(input("Opción elegida: "))
            if opcion==1:
                print("Empiece")
            elif opcion==2:
                print("Listado:")
                print("Carlos, Merzian, Melany, Pierina")
            elif opcion==3:
                print("Hasta luego :)")
                break
            else:
                print("Opción incorrecta. Ingrese 1, 2 o 3")
# Solicitar al usuario el ingreso de una frase y de una letra (que puede o no
# estar en la frase). Recorrer la frase, carácter a carácter, comparando con la
# letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en
# esa posición (imprimiendo la posición) y continuar. Si se encuentra una
# coincidencia, indicar en qué posición se encontró y finalizar la ejecución
    def Ejercicio6_13(self):
        frasecjsg=input("Ingrese una frase: ")
        l=input("Inserte una letra para buscar su posición: ")
        i=0
        while i!=len(frasecjsg):
            if l!=frasecjsg[i]:
                print("No se encontró en la posición", i)
                i+=1
                continue
            print("Esta en la posición", i)
            break         
# Crear un programa que permita al usuario ingresar los montos de las compras
# de un cliente (se desconoce la cantidad de datos que cargará, la cual puede
# cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario
# ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese
# un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta
# que, si las ventas superan el total de $1000, se le debe aplicar un 10% de
# descuento.
    def Ejercicio6_14(self):
        totalcjsg=0
        montocjsg=float(input("Ingrese un monto de una venta: $"))
        while montocjsg!=0:
            if montocjsg<0:
                print("Monto no válido.")
            else:
                totalcjsg+=montocjsg
            montocjsg=float(input("Ingrese un monto de una venta: $"))
        if totalcjsg>1000:
            totalcjsg-=totalcjsg*0.1
        print("Monto total a pagar: $", totalcjsg) 
# Crear un programa que solicite el ingreso de números enteros positivos, hasta
# que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares
# y cuántos impares tiene.
# Página 25 de 26
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos
# en total.
    def Ejercicio6_16(self): 
        numero=int(input("numero: "))
        totalPares=0
        totalImpares=0
        while numero!=0:
            pares=0
            impares=0
            while numero!=0:   
                ultimodigito=numero%10
                if ultimodigito%2==0:
                    pares+=1
                    totalPares+=1
                else:
                    impares+=1
                    totalImpares+=1
                numero=numero//10
            print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
            numero=int(input("Otro número: "))
        print("Total de dígitos pares:", totalPares)
        print("Total de dígitos impares:", totalImpares)
# Crear un programa que permita al usuario ingresar títulos de libros por
# teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que
# el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”)
# se considera que termina una línea. Por cada línea completa, informar cuántos
# dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de
# libros que componen en esa línea). Finalmente, informar cuántas líneas
# completas se ingresaron.
# **Ejemplo de ejecución:**
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.
    def Ejercicio6_17(self): 
        lineas=0
        digitos="0123456789"
        cantidadDigitos=0
        cadena=input("Cadena: ")
        while cadena!="*":
            for caracter in cadena:
                if caracter in digitos:
                    cantidadDigitos+=1
            if cadena=="/":
                lineas+=1
                print("Aparecen ", cantidadDigitos, " dígitos en la línea")
                cantidadDigitos=0
            cadena=input("Cadena: ")
        print("Se leyeron ",lineas," líneas completas")
# Escribir un programa que solicite el ingreso de una cantidad indeterminada
# de números mayores que 1, finalizando cuando se reciba un cero. Imprimir
# la cantidad de números primos ingresados.
    def Ejercicio6_18(self): 
        cantidad=0
        n=int(input("Ingrese un numero: "))
        while n!=0:
            primo=True
            for i in range(2,n):
                if n%i==0:
                    primo=False
                    break
            if primo:
                cantidad+=1
                n=int(input("Ingrese un numero: "))
            print("Loa cantidad de numeros primos: ", cantidad)
# Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra
# más larga (en caso de haber más de una, mostrar la primera) y cuántas
# palabras había. Precondición: se tomará como separador de palabras al
# carácter “ “ (espacio), ya sea uno o más.
    def Ejercicio6_19(self): 
        frasecjsg=input("Inserte una frase: ").strip()
        cantidadcjsg=0
        len_p_mas_larga=0
        while len(frasecjsg) != 0:
            cantidadcjsg=cantidadcjsg+1
            i=frasecjsg.find(" ")
            if i != -1:
                palabra=frasecjsg[0:i]
                while i < len(frasecjsg) and frasecjsg[i] == " ":
                    i=i+1
                frasecjsg=frasecjsg[i:]
            else:
                palabra=frasecjsg
                frasecjsg=""
            if len(palabra) > len_p_mas_larga:
                len_p_mas_larga=len(palabra)
                p_mas_larga=palabra
        if cantidadcjsg > 0:
            print("La palabra más larga:", p_mas_larga)
        print("La cantidad de palabras es:", cantidadcjsg)

estructura = Ejercicios()
estructura.Ejercicio6_2()
#Reemplace la linea 375 por el ejercicio que desea ejecutar
