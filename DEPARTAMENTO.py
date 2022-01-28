class DepartamentoCarlitos:
    secuencia = 0  #Es un atributo de clase ya que funciona para todas las instancias
    departamentos = []
    def __init__(self,descrip):
        DepartamentoCarlitos.secuencia +=1
        self.codigo= DepartamentoCarlitos.secuencia  #Atributo de instancia solo pertenecen a la instancia en la que fueron creadas
        self.departamento= descrip

    def registro(self):
        return {"codigo":self.codigo, "departamento":self.departamento}