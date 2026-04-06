class Plato:

    def __init__(self, nombre, precio_base, es_vegetariano):
        self.nombre = nombre
        self._precio_base = precio_base
        self.es_vegetariano = es_vegetariano

    def precio(self):
        return self._precio_base
    
    def descripcion(self):
        if self.es_vegetariano:
            tipo = "Vegetariano"
        else:
            tipo = "Estandar"
            
        return f"{self.nombre} - {tipo} - Precio: ${self.precio():.2f}"
