from comensal import Comensal
from menudia import MenuDia
from plato import Plato
from procesador_venta import ProcesadorVenta


plato_estandar1 = Plato("Bandeja paisa", 12000, False)
plato_estandar2 = Plato("Sudado de pollo", 10000, False)
plato_vegetariano1 = Plato("Cazuela de lentejas", 9500, True)
plato_vegetariano2 = Plato("Ensalada mediterránea", 8500, True)

menu = MenuDia("2026-04-01")
menu.agregar_plato(plato_estandar1)
menu.agregar_plato(plato_estandar2)
menu.agregar_plato(plato_vegetariano1)
menu.agregar_plato(plato_vegetariano2)

procesador = ProcesadorVenta()


while True:
    print("\n=== CAFETERÍA NutriUTP ===")
    print("1. Registrar almuerzo")
    print("2. Ver reporte del dia")
    print("3. Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        id_estudiante = input("ID estudiante: ")
        tipo_subsidio = input("Tipo de subsidio (A/B/C/ninguno): ").upper()
        estudiante = Comensal(id_estudiante, tipo_subsidio)

        preferencia = input("Preferencia (estandar/vegetariano): ").lower()
        opciones_filtradas = menu.seleccionar_opcion(preferencia)

        if not opciones_filtradas:
            print("No hay platos disponibles.")
        else:
            print("\n--- Platos disponibles ---")
            for i, plato in enumerate(opciones_filtradas):
                print(f"{i+1}. {plato.descripcion()}")

            numero = int(input("Elija un numero: ")) - 1
            plato_elegido = opciones_filtradas[numero]

            if procesador.validar_pago(estudiante):
                tiquete = procesador.generar_tiquete(estudiante, plato_elegido)
                print(tiquete)

    elif opcion == "2":
        procesador.generar_reporte()

    elif opcion == "3":
        print("Hasta luego.")
        break