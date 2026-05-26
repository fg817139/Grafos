

DESCRIPCION DEL PROYECTO

Este proyecto implementa un sistema de navegacion para el campus de la Universidad de Medellin (UDEM). Utiliza estructuras de grafos para encontrar rutas optimas entre diferentes ubicaciones del campus.

El sistema ofrece multiples opciones de busqueda de rutas:
- Ruta mas corta: distancia minima entre dos puntos
- Ruta mas rapida: tiempo minimo considerando velocidad de transito
- Ruta con menor congestion: evita areas transitadas
- Ruta accesible: rutas para personas con movilidad reducida
- Tour de visitantes: recorrido que pasa por todas las ubicaciones importantes

COMO EJECUTAR EL PROYECTO

Requisitos:
- Python 3.x instalado

Pasos:
1. Navega a la carpeta Pratica
2. Ejecuta el programa con:
   python main.py
3. Selecciona una opcion del menu principal
4. Sigue las indicaciones en pantalla para encontrar rutas o explorar el campus

El programa abre un menu interactivo donde puedes:
- Buscar ruta entre dos ubicaciones
- Ver tour para visitantes
- Listar todas las ubicaciones del campus
- Salir del programa

SUPUESTOS ASUMIDOS

- El campus esta modelado como un grafo conexo donde cada ubicacion (bloque, edificio) es un nodo
- Las aristas entre ubicaciones tienen atributos: distancia, tiempo, congestion y accesibilidad
- La distancia esta en metros
- El tiempo esta en minutos
- El nivel de congestion es una escala de 1 a 5
- Una ruta es accesible si todos sus segmentos tienen la propiedad accesible = True
- Se asume que el usuario tiene acceso a la consola/terminal para ejecutar el programa
- No hay autenticacion requerida para acceder al sistema
- Los datos del campus (ubicaciones y conexiones) estan predefinidos en campus_udem.py


