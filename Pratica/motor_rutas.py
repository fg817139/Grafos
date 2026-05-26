from typing import Tuple, List, Dict, Any
from grafos import GrafoMatriz

class MotorRutas:
    
    
    def __init__(self, campus):
        self.campus = campus
        self.grafo = campus.grafo
    
    def _reconstruir_ruta(self, predecesores: Dict[Any, Any], destino: Any) -> List[Any]:
        
        ruta = []
        actual = destino
        
        while actual is not None:
            ruta.insert(0, actual)
            actual = predecesores.get(actual)
        
        return ruta
    
    def dijkstra_distancia(self, origen: Any, destino: Any) -> Tuple[float, List[Any], str]:
        if origen not in self.grafo.vertices or destino not in self.grafo.vertices:
            return (float('inf'), [], "Uno o ambos vértices no existen")
        
        distancias = {v: float('inf') for v in self.grafo.vertices}
        distancias[origen] = 0
        predecesores = {v: None for v in self.grafo.vertices}
        visitados = set()
        
        while len(visitados) < len(self.grafo.vertices):
            minimo = float('inf')
            vertice_actual = None
            
            for v in self.grafo.vertices:
                if v not in visitados and distancias[v] < minimo:
                    minimo = distancias[v]
                    vertice_actual = v
            
            if vertice_actual is None or minimo == float('inf'):
                break
            
            visitados.add(vertice_actual)
            vecinos = self.campus.obtener_vecinos_transitables(vertice_actual)
            
            for vecino in vecinos:
                arista = self.campus.obtener_arista(vertice_actual, vecino)
                if arista and arista.es_transitable():
                    nueva_dist = distancias[vertice_actual] + arista.distancia
                    if nueva_dist < distancias[vecino]:
                        distancias[vecino] = nueva_dist
                        predecesores[vecino] = vertice_actual
        
        ruta = self._reconstruir_ruta(predecesores, destino)
        dist_total = distancias[destino]
        
        if dist_total == float('inf'):
            return (float('inf'), [], "No hay ruta disponible")
        
        exp = f"Ruta optimizada por DISTANCIA MINIMA: {dist_total:.0f} metros."
        return (dist_total, ruta, exp)
    
    def dijkstra_tiempo(self, origen: Any, destino: Any) -> Tuple[float, List[Any], str]:
    
        if origen not in self.grafo.vertices or destino not in self.grafo.vertices:
            return (float('inf'), [], "Uno o ambos vértices no existen")
        
        tiempos = {v: float('inf') for v in self.grafo.vertices}
        tiempos[origen] = 0
        predecesores = {v: None for v in self.grafo.vertices}
        visitados = set()
        
        while len(visitados) < len(self.grafo.vertices):
            minimo = float('inf')
            vertice_actual = None
            
            for v in self.grafo.vertices:
                if v not in visitados and tiempos[v] < minimo:
                    minimo = tiempos[v]
                    vertice_actual = v
            
            if vertice_actual is None or minimo == float('inf'):
                break
            
            visitados.add(vertice_actual)
            vecinos = self.campus.obtener_vecinos_transitables(vertice_actual)
            
            for vecino in vecinos:
                arista = self.campus.obtener_arista(vertice_actual, vecino)
                if arista and arista.es_transitable():
                    nuevo_tiempo = tiempos[vertice_actual] + arista.tiempo
                    if nuevo_tiempo < tiempos[vecino]:
                        tiempos[vecino] = nuevo_tiempo
                        predecesores[vecino] = vertice_actual
        
        ruta = self._reconstruir_ruta(predecesores, destino)
        tiempo_total = tiempos[destino]
        
        if tiempo_total == float('inf'):
            return (float('inf'), [], "No hay ruta disponible")
        
        exp = f"Ruta optimizada por TIEMPO MINIMO: {tiempo_total:.1f} minutos."
        return (tiempo_total, ruta, exp)
    
    def dijkstra_congestion(self, origen: Any, destino: Any) -> Tuple[float, List[Any], str]:
        
        if origen not in self.grafo.vertices or destino not in self.grafo.vertices:
            return (float('inf'), [], "Uno o ambos vértices no existen")
        
        congestiones = {v: float('inf') for v in self.grafo.vertices}
        congestiones[origen] = 0
        predecesores = {v: None for v in self.grafo.vertices}
        visitados = set()
        
        while len(visitados) < len(self.grafo.vertices):
            minimo = float('inf')
            vertice_actual = None
            
            for v in self.grafo.vertices:
                if v not in visitados and congestiones[v] < minimo:
                    minimo = congestiones[v]
                    vertice_actual = v
            
            if vertice_actual is None or minimo == float('inf'):
                break
            
            visitados.add(vertice_actual)
            vecinos = self.campus.obtener_vecinos_transitables(vertice_actual)
            
            for vecino in vecinos:
                arista = self.campus.obtener_arista(vertice_actual, vecino)
                if arista and arista.es_transitable():
                    nueva_cong = congestiones[vertice_actual] + arista.congestion
                    if nueva_cong < congestiones[vecino]:
                        congestiones[vecino] = nueva_cong
                        predecesores[vecino] = vertice_actual
        
        ruta = self._reconstruir_ruta(predecesores, destino)
        cong_total = congestiones[destino]
        
        if cong_total == float('inf'):
            return (float('inf'), [], "No hay ruta disponible")
        
        exp = f"Ruta optimizada por MENOR CONGESTION: {cong_total:.1f} puntos."
        return (cong_total, ruta, exp)
    
    def dijkstra_accesibilidad(self, origen: Any, destino: Any) -> Tuple[float, List[Any], str]:
        if origen not in self.grafo.vertices or destino not in self.grafo.vertices:
            return (float('inf'), [], "Uno o ambos vértices no existen")
        
        distancias = {v: float('inf') for v in self.grafo.vertices}
        distancias[origen] = 0
        predecesores = {v: None for v in self.grafo.vertices}
        visitados = set()
        
        while len(visitados) < len(self.grafo.vertices):
            minimo = float('inf')
            vertice_actual = None
            
            for v in self.grafo.vertices:
                if v not in visitados and distancias[v] < minimo:
                    minimo = distancias[v]
                    vertice_actual = v
            
            if vertice_actual is None or minimo == float('inf'):
                break
            
            visitados.add(vertice_actual)
            vecinos = self.campus.obtener_vecinos_transitables(vertice_actual)
            
            for vecino in vecinos:
                arista = self.campus.obtener_arista(vertice_actual, vecino)
                if arista and arista.es_transitable() and arista.accesible:
                    nueva_dist = distancias[vertice_actual] + arista.distancia
                    if nueva_dist < distancias[vecino]:
                        distancias[vecino] = nueva_dist
                        predecesores[vecino] = vertice_actual
        
        ruta = self._reconstruir_ruta(predecesores, destino)
        dist_total = distancias[destino]
        
        if dist_total == float('inf'):
            return (float('inf'), [], "No hay ruta accesible disponible")
        
        exp = f"Ruta optimizada para ACCESIBILIDAD: {dist_total:.0f} metros."
        return (dist_total, ruta, exp)
    
    def obtener_ruta_optima(self, origen: Any, destino: Any, criterio: str) -> Tuple[float, List[Any], str]:
        """Obtiene la ruta óptima según el criterio especificado."""
        criterios = {
            "distancia": self.dijkstra_distancia,
            "tiempo": self.dijkstra_tiempo,
            "congestion": self.dijkstra_congestion,
            "accesibilidad": self.dijkstra_accesibilidad
        }
        
        if criterio not in criterios:
            return (float('inf'), [], f"Criterio '{criterio}' no reconocido")
        
        return criterios[criterio](origen, destino)
