class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        #como está definida como privada me tengo que crear
        #un método para poder cambiar el valor.
        
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
        
    def propiedadPrivada(self, valor = None):
        if valor == None:
            #actua como getter
            return self._propiedad_privada
        else:
            #actua como setter
            self.__propiedad_privada = valor
            
        
    def __str__(self):
        return "ClaseConGetterySetter con PropiedadPrivada -> {}".formar(self.__propiedad_privada)
    
        
if __name__ == "__main__":
    c = ClaseConGetterySetter()