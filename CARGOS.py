class CargosCarlitos:
    secuencia = 2                                                   #Es un atributo de clase ya que funciona para todas las instancias
    cargos = [{"codigo":1,"cargo":"Analista"}, {"codigo":2,"cargo":"Jefe"}]
    def __init__(self,descrip):
        CargosCarlitos.secuencia +=1
        self.codigo= CargosCarlitos.secuencia                         #Atributo de instancia solo pertenecen a la instancia en la que fueron creadas
        self.cargo= descrip
        
    def registro(self):
        return {"codigo":self.codigo , "cargo":self.cargo}
        
                
        
    