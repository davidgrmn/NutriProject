# NutriProject - Sistema de Cafetería Estudiantil

Sistema de gestión de almuerzos para la cafetería de la Universidad 
Tecnológica de Pereira, desarrollado como proyecto de Programación 4.

## Descripción
Permite administrar el menú diario, procesar subsidios estudiantiles 
y generar tiquetes de venta, aplicando principios de desacoplamiento 
de software.

## Principios de diseño aplicados
- **SRP**: cada clase tiene una única responsabilidad
- **Encapsulamiento**: atributos internos protegidos con `_`
- **Inyección de dependencias**: `ProcesadorVenta` recibe sus 
  colaboradores como parámetros

## Estructura del proyecto
    nutriutp/
    ├── plato.py            # Gestión de cada plato del menú
    ├── menu_dia.py         # Oferta gastronómica del día
    ├── comensal.py         # Perfil del estudiante y subsidios
    ├── procesador_venta.py # Coordinación de transacciones
    └── main.py             # Punto de entrada

## Cómo ejecutar
Requiere Python 3. Desde la carpeta del proyecto:
    python main.py
