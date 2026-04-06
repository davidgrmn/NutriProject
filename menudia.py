from plato import Plato

class MenuDia:

    def __init__(self, fecha):
        self.fecha = fecha
        self._opciones = []
    
    def agregar_plato(self, plato):
        self._opciones.append(plato)
    
    def _aislar_seleccion(self, es_vegetariano):
        return [plato for plato in self._opciones if plato.es_vegetariano == es_vegetariano]

    def seleccionar_opcion(self, tipo_preferencia):
        if tipo_preferencia == "vegetariano":
            return self._aislar_seleccion(True)
        else:
            return self._aislar_seleccion(False)
    
    

