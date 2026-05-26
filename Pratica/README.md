# Navegación Campus UDEM

Sistema para encontrar rutas en el campus. Elige dónde quieres ir y cómo quieres llegar por distancia, tiempo, accesibilidad.

## ¿Qué hace?

#Encuentra el camino más corto entre dos puntos del campus
#Ofrece diferentes tipos de rutas: la más rápida, la menos transitada la más accesible
#Genera un recorrido que pasa por todas las ubicaciones importantes
#Evita rutas bloqueadas o en mantenimiento

## Cómo usarlo

```bash
python main.py
```

Se abre un menú interactivo donde puedes:

#Ver ubicaciones = (Lista todos los bloques del campus)
#Buscar ruta = (Elige origen y destino y tipo de ruta) (corta, rápida, accesible)
#Tour de visitantes = (Recorrido que pasa por todo el campus)
#Salir

Responde las preguntas que aparecen y listo te muestrara el camino.

## Archivos principales

main.py = El programa, ejecuta esto
campus_udem.py = Mapa del campus con todas las conexiones
motor_rutas.py = Los algoritmos que encuentran las rutas
tour_visitantes.py = El recorrido para visitantes

## Rápido y simple

No hay configuración complicada. Solo ejecuta y elige dónde quieres ir.
