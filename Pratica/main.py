from campus_udem import CampusUdeM
from motor_rutas import MotorRutas
from tour_visitantes import TourVisitantes

def mostrar_menu_principal():
    
    print("NAVEGACIÓN CAMPUS UDEM".center(70))
    print("\n1. Encontrar ruta entre dos ubicaciones")
    print("2. Ver tour para visitantes (todas las ubicaciones)")
    print("3. Listar todas las ubicaciones del campus")
    print("4. Salir")
    print("\n" + "-"*70)

def mostrar_menu_criterios():
    print("\nSeleccione el criterio de búsqueda:")
    print("1. Distancia mínima (Ruta más corta)")
    print("2. Tiempo mínimo (Ruta más rápida)")
    print("3. Menor congestión")
    print("4. Accesible (Para personas con movilidad reducida)")
    print("-"*70)

def seleccionar_ubicacion(campus, prompt=""):
    ubicaciones = campus.obtener_ubicaciones()
    
    while True:
        print(f"\n{prompt}")
        for i, ubicacion in enumerate(ubicaciones, 1):
            print(f"{i}. {ubicacion}")
        
        try:
            opcion = int(input("\nIngrese el número de la ubicación: "))
            if 1 <= opcion <= len(ubicaciones):
                return ubicaciones[opcion - 1]
            else:
                print("Opción no válida, vuelve a intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido.")

def procesar_criterio(opcion):
    criterios = {
        "1": "distancia",
        "2": "tiempo",
        "3": "congestion",
        "4": "accesibilidad"
    }
    return criterios.get(opcion, None)

def mostrar_ruta(campus, costo, ruta, explicacion, unidad=""):
    
    print("RUTA ENCONTRADA".center(70))
    
    print(f"\n{explicacion}")
    
    if ruta:
        print(f"\nCosto total: {costo:.1f} {unidad}")
        print("\nSecuencia de ubicaciones:")
        for i, ubicacion in enumerate(ruta, 1):
            if i < len(ruta):
                arista = campus.obtener_arista(ruta[i-1], ruta[i])
                if arista:
                    print(f"  {i}. {ubicacion}")
                    print(f"     ↓ (Distancia: {arista.distancia:.0f}m, "
                          f"Tiempo: {arista.tiempo:.1f}min, "
                          f"Congestión: {arista.congestion}/5, "
                          f"Accesible: {'Sí' if arista.accesible else 'No'})")
            else:
                print(f"  {i}. {ubicacion} (DESTINO)")
    else:
        print("\nNo se encontró ruta disponible entre las ubicaciones seleccionadas.")
    
    print("\n" + "="*70)

def mostrar_tour(costo, tour, descripcion):
    
    print("TOUR PARA VISITANTES".center(70))
    print(f"\n{descripcion}")
    
    if tour:
        print(f"\nTotal de ubicaciones a visitar: {len(tour)}")
        print("\nItinerario:")
        for i, ubicacion in enumerate(tour, 1):
            print(f"  {i}. {ubicacion}")
    
    print("\n" + "="*70)

def main():
    campus = CampusUdeM()
    motor = MotorRutas(campus)
    tour_gen = TourVisitantes(campus)
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            
            print("\n" + "-"*70)
            origen = seleccionar_ubicacion(campus, "Seleccione ubicación de ORIGEN:")
            destino = seleccionar_ubicacion(campus, "Seleccione ubicación de DESTINO:")
            
            if origen == destino:
                print("\n El origen y destino no pueden repetir.")
                continue
            
            mostrar_menu_criterios()
            criterio_opcion = input("Seleccione un criterio: ").strip()
            criterio = procesar_criterio(criterio_opcion)
            
            if criterio is None:
                print("Criterio no válido.")
                continue
            
            costo, ruta, explicacion = motor.obtener_ruta_optima(origen, destino, criterio)
            
            unidad_map = {
                "distancia": "metros",
                "tiempo": "minutos",
                "congestion": "puntos",
                "accesibilidad": "metros"
            }
            unidad = unidad_map.get(criterio, "")
            
            mostrar_ruta(campus, costo, ruta, explicacion, unidad)
        
        elif opcion == "2":
            costo, tour, descripcion = tour_gen.generar_tour_visitantes()
            mostrar_tour(costo, tour, descripcion)
        
        elif opcion == "3":
            campus.listar_ubicaciones()
        
        elif opcion == "4":
            print("\nGracias por usar el Sistema")
            print("Hasta luego.\n")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
