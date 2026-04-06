# NutriProject - Sistema de Cafetería Estudiantil

Sistema de gestion de almuerzos para la cafeteria de una universidad.

## Descripcion
Permite administrar el menu diario, procesar subsidios estudiantiles 
y generar tiquetes de venta, aplicando principios de desacoplamiento 
de software.

## Principios de diseño aplicados
- **SRP**: cada clase tiene una unica responsabilidad
- **Encapsulamiento**: atributos internos protegidos con `_`
- **Inyección de dependencias**: `ProcesadorVenta` recibe sus 
  colaboradores como parametros

## Estructura del proyecto
    nutriproj/
    ├── plato.py            # Gestion de cada plato del menu
    ├── menu_dia.py         # Oferta gastronómica del día
    ├── comensal.py         # Perfil del estudiante y subsidios
    ├── procesador_venta.py # Coordinacion de transacciones
    └── main.py             # Main

## Cómo ejecutar
Requiere Python 3. Desde la carpeta del proyecto:
    python main.py
