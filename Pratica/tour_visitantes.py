from typing import List, Tuple

class TourVisitantes:
    
    def __init__(self, campus):
        self.campus = campus
        self.grafo = campus.grafo
    
    def _calcular_mst(self) -> Tuple[float, List[Tuple[str, str, float]]]:
        
        if len(self.grafo.vertices) == 0:
            return (0, [])
        
        vertices_visitados = [self.grafo.vertices[0]]
        conexiones_arbol = []
        peso_total = 0
        
        while len(vertices_visitados) < len(self.grafo.vertices):
            peso_minimo = float('inf')
            origen_elegido = None
            destino_elegido = None
            arista_elegida = None
            
            
            for vertice_visitado in vertices_visitados:
                vecinos = self.grafo.obtenerVecinos(vertice_visitado)
                for vecino in vecinos:
                    if vecino not in vertices_visitados:
                        arista = self.grafo.obtenerArista(vertice_visitado, vecino)
                        if arista and arista.es_transitable() and arista.distancia < peso_minimo:
                            peso_minimo = arista.distancia
                            origen_elegido = vertice_visitado
                            destino_elegido = vecino
                            arista_elegida = arista
            
            if destino_elegido is not None:
                vertices_visitados.append(destino_elegido)
                conexiones_arbol.append((origen_elegido, destino_elegido, peso_minimo))
                peso_total += peso_minimo
        
        return (peso_total, conexiones_arbol)
    
    def _construir_tour(self, mst_conexiones: List[Tuple[str, str, float]]) -> List[str]:
        
        if not mst_conexiones:
            return self.grafo.vertices[:1] if self.grafo.vertices else []
        
        arbol_adyacencia = {}
        for origen, destino, _ in mst_conexiones:
            if origen not in arbol_adyacencia:
                arbol_adyacencia[origen] = []
            if destino not in arbol_adyacencia:
                arbol_adyacencia[destino] = []
            
            arbol_adyacencia[origen].append(destino)
            arbol_adyacencia[destino].append(origen)
        
        
        tour = []
        visitados = set()
        
        def dfs(nodo):
            visitados.add(nodo)
            tour.append(nodo)
            
            if nodo in arbol_adyacencia:
                for vecino in arbol_adyacencia[nodo]:
                    if vecino not in visitados:
                        dfs(vecino)
        
        dfs(self.grafo.vertices[0])
        
        return tour
    
    def _calcular_distancia_tour(self, tour: List[str]) -> float:
        
        distancia_total = 0
        
        for i in range(len(tour) - 1):
            arista = self.grafo.obtenerArista(tour[i], tour[i + 1])
            if arista:
                distancia_total += arista.distancia
        
        return distancia_total
    
    def generar_tour_visitantes(self) -> Tuple[float, List[str], str]:
        
        if len(self.grafo.vertices) == 0:
            return (0, [], "El campus no tiene ubicaciones")
        
        if len(self.grafo.vertices) == 1:
            return (0, self.grafo.vertices, "Solo hay una ubicación en el campus")
        
        
        distancia_mst, mst_conexiones = self._calcular_mst()
        
        if not mst_conexiones:
            return (0, [self.grafo.vertices[0]], "No es posible conectar todas las ubicaciones")
        
        
        tour = self._construir_tour(mst_conexiones)
        
        distancia_tour = self._calcular_distancia_tour(tour)
        
        descripcion = (
            f"Tour para VISITANTES: Recorre todas las {len(tour)} ubicaciones del campus "
            f"sin repetir ninguna, con una distancia total de {distancia_tour:.0f} metros. "
            f"El tour está optimizado basándose en el Árbol de Expansión Mínimo para minimizar "
            f"la distancia total del recorrido."
        )
        
        return (distancia_tour, tour, descripcion)
