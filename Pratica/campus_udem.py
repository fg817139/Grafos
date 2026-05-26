from typing import Dict, Tuple
from grafos import GrafoMatriz
from arista import Arista


class CampusUdeM:
    
    def __init__(self):
        self.grafo = GrafoMatriz()
        self.aristas: Dict[Tuple[int, int], Arista] = {}
        self._inicializar_campus()
    
    def _inicializar_campus(self):
        
        ubicaciones = [
            "Bloque 1 - Coliseo Cubierto",
            "Bloque 2 - Bienestar Universitario",
            "Bloque 3 - Centro de Laboratorios",
            "Bloque 4 - Ingenierías",
            "Bloque 4 - Zona de Comidas",
            "Bloque 5 - Ciencias Básicas",
            "Bloque 6 - Ciencias Económicas",
            "Bloque 7 - Contaduría",
            "Bloque 8 - Cancha Central",
            "Bloque 9 - Producción de Televisión",
            "Bloque 10 - Comunicación e Idiomas",
            "Bloque 11 - Audiovisuales",
            "Bloque 12 - Ciencias Sociales",
            "Bloque 13 - Biblioteca",
            "Bloque 14 - Centro de Cómputo",
            "Bloque 15 - Medios Educativos",
            "Bloque 16 - Derecho",
            "Bloque 17 - Teatro"
        ]
        
        for ubicacion in ubicaciones:
            self.grafo.agregarVertice(ubicacion)
        
        conexiones = [
            ("Bloque 1 - Coliseo Cubierto", "Bloque 2 - Bienestar Universitario", 90, 3, 2, True, "disponible"),
            ("Bloque 1 - Coliseo Cubierto", "Bloque 3 - Centro de Laboratorios", 130, 4, 3, True, "disponible"),
            ("Bloque 2 - Bienestar Universitario", "Bloque 3 - Centro de Laboratorios", 80, 3, 2, True, "disponible"),
            ("Bloque 2 - Bienestar Universitario", "Bloque 8 - Cancha Central", 120, 4, 2, True, "disponible"),
            ("Bloque 3 - Centro de Laboratorios", "Bloque 4 - Ingenierías", 100, 4, 3, True, "disponible"),
            ("Bloque 4 - Ingenierías", "Bloque 4 - Zona de Comidas", 40, 2, 3, True, "disponible"),
            ("Bloque 4 - Ingenierías", "Bloque 5 - Ciencias Básicas", 70, 3, 2, True, "disponible"),
            ("Bloque 4 - Zona de Comidas", "Bloque 5 - Ciencias Básicas", 60, 3, 4, True, "disponible"),
            ("Bloque 4 - Zona de Comidas", "Bloque 8 - Cancha Central", 90, 4, 4, True, "disponible"),
            ("Bloque 5 - Ciencias Básicas", "Bloque 6 - Ciencias Económicas", 85, 3, 2, True, "disponible"),
            ("Bloque 6 - Ciencias Económicas", "Bloque 7 - Contaduría", 75, 3, 2, True, "disponible"),
            ("Bloque 6 - Ciencias Económicas", "Bloque 8 - Cancha Central", 110, 4, 3, True, "disponible"),
            ("Bloque 7 - Contaduría", "Bloque 11 - Audiovisuales", 95, 4, 2, True, "disponible"),
            ("Bloque 8 - Cancha Central", "Bloque 13 - Biblioteca", 140, 5, 3, True, "disponible"),
            ("Bloque 8 - Cancha Central", "Bloque 14 - Centro de Cómputo", 160, 6, 3, True, "disponible"),
            ("Bloque 9 - Producción de Televisión", "Bloque 10 - Comunicación e Idiomas", 70, 3, 2, True, "disponible"),
            ("Bloque 9 - Producción de Televisión", "Bloque 11 - Audiovisuales", 90, 4, 2, True, "disponible"),
            ("Bloque 10 - Comunicación e Idiomas", "Bloque 11 - Audiovisuales", 60, 2, 2, True, "disponible"),
            ("Bloque 11 - Audiovisuales", "Bloque 12 - Ciencias Sociales", 65, 3, 2, True, "disponible"),
            ("Bloque 12 - Ciencias Sociales", "Bloque 13 - Biblioteca", 70, 3, 2, True, "disponible"),
            ("Bloque 13 - Biblioteca", "Bloque 14 - Centro de Cómputo", 80, 3, 2, True, "disponible"),
            ("Bloque 14 - Centro de Cómputo", "Bloque 15 - Medios Educativos", 75, 3, 2, True, "disponible"),
            ("Bloque 15 - Medios Educativos", "Bloque 16 - Derecho", 90, 4, 2, True, "disponible"),
            ("Bloque 16 - Derecho", "Bloque 17 - Teatro", 85, 3, 2, True, "disponible"),
            ("Bloque 13 - Biblioteca", "Bloque 16 - Derecho", 150, 6, 3, True, "disponible"),
            ("Bloque 14 - Centro de Cómputo", "Bloque 17 - Teatro", 170, 7, 3, True, "disponible"),
            ("Bloque 3 - Centro de Laboratorios", "Bloque 8 - Cancha Central", 130, 5, 3, False, "disponible"),
            ("Bloque 5 - Ciencias Básicas", "Bloque 9 - Producción de Televisión", 180, 7, 4, False, "disponible"),
            ("Bloque 4 - Zona de Comidas", "Bloque 13 - Biblioteca", 220, 8, 5, True, "mantenimiento"),
            ("Bloque 11 - Audiovisuales", "Bloque 14 - Centro de Cómputo", 130, 5, 3, True, "bloqueado")
        ]
        
        for origen, destino, distancia, tiempo, congestion, accesible, estado in conexiones:
            self.grafo.agregarConexion(origen, destino, dirigido=False, peso=distancia)
            
            arista = Arista(distancia, tiempo, congestion, accesible, estado)
            pos1 = self.grafo.vertices.index(origen)
            pos2 = self.grafo.vertices.index(destino)
            self.aristas[(pos1, pos2)] = arista
            self.aristas[(pos2, pos1)] = arista
    
    def obtener_ubicaciones(self):
        return self.grafo.vertices
    
    def obtener_vecinos_transitables(self, ubicacion):
        if ubicacion not in self.grafo.vertices:
            return []
        
        pos = self.grafo.vertices.index(ubicacion)
        vecinos = []
        
        for i in range(self.grafo.tamano):
            if self.grafo.matrizAdy[pos][i] != 0:
                arista = self.aristas.get((pos, i))
                if arista and arista.es_transitable():
                    vecinos.append(self.grafo.vertices[i])
        
        return vecinos
    
    def obtener_arista(self, ubicacion1, ubicacion2):
        if ubicacion1 not in self.grafo.vertices or ubicacion2 not in self.grafo.vertices:
            return None
        
        pos1 = self.grafo.vertices.index(ubicacion1)
        pos2 = self.grafo.vertices.index(ubicacion2)
        
        return self.aristas.get((pos1, pos2))
    
    def listar_ubicaciones(self):
        print("\n UBICACIONES DEL CAMPUS UDEM ")
        for i, ubicacion in enumerate(self.grafo.vertices, 1):
            print(f"{i}. {ubicacion}")
        print()