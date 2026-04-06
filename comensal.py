class Comensal:
    def __init__(self, id_estudiante, tipo_subsidio):
        self.id_estudiante = id_estudiante
        self.tipo_subsidio = tipo_subsidio
    
    def calcular_descuento(self, valor_plato):
        if self.tipo_subsidio == "A":
            precio_final = valor_plato - (valor_plato*0.10)

        elif self.tipo_subsidio == "B":
            precio_final = valor_plato - (valor_plato*0.15)
        
        elif self.tipo_subsidio == "C":
            precio_final = valor_plato - (valor_plato*0.30)
        
        else:
            precio_final = valor_plato
        
        return precio_final
        