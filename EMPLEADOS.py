class EmpleadosCarlitos:
    secuencia =2
    Empleados = [{"codigo":1,"nombre":"Merzian", "cedula":"0926015850", "cargo":1,"departamento":1,"sueldo":7500.50},
                 {"codigo":2,"nombre":"Daniel","cedula":"0914592522","cargo":2,"departamento":2,"sueldo":6050.70}]

    def __init__(self, nombre, cedula, codCargo, codDepartamento, sueldo):
        EmpleadosCarlitos.secuencia +=1
        self.codigo = EmpleadosCarlitos.secuencia 
        self.nombre = nombre
        self.cedula = cedula
        self.cargo = codCargo
        self.departamento = codDepartamento
        self.sueldo = sueldo

    def registro(self):
        return {"codigo":self.codigo, "nombre": self.nombre,"cedula":self.cedula, "cargo":self.cargo, "departamento":self.departamento, "sueldo":self.sueldo}