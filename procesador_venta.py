class ProcesadorVenta:

    def __init__(self):
        self.ventas = []

    def generar_tiquete(self, estudiante, plato):
        precio_final = estudiante.calcular_descuento(plato.precio())

        self.ventas.append({
            "plato": plato.nombre,
            "precio": precio_final
        })

        tiquete = f"""
        ---- TIQUETE CAFETERIA NutriUTP ----
        Estudiante: {estudiante.id_estudiante}
        Subsidio:   {estudiante.tipo_subsidio}
        Plato:      {plato.descripcion()}
        Precio final:     ${precio_final}
        ------------------------------------
        """
        return tiquete
    
    def generar_reporte(self):
        print("\n=== REPORTE DEL DIA ===")
        for venta in self.ventas:
            print(f"{venta['plato']} - ${venta['precio']}")
        total = sum(v['precio'] for v in self.ventas)
        print(f"\nTotal recaudado: ${total}")
    
    def validar_pago(self, estudiante):
        # Aqui iria una llamada a tesorería
        print(f"Validando pago con tesoreria para estudiante {estudiante.id_estudiante}...")
        return True
    


