class Arista:
    
    def __init__(self, distancia: float, tiempo: float, congestion: int, accesible: bool, estado: str):
       
        self.distancia = distancia
        self.tiempo = tiempo
        self.congestion = congestion
        self.accesible = accesible
        self.estado = estado
    
    def es_transitable(self) -> bool:
        return self.estado == "disponible"
    
    def __str__(self) -> str:
        return f"Arista(dist={self.distancia}m, tiempo={self.tiempo}min, congestion={self.congestion}, accesible={self.accesible}, estado={self.estado})"
    
    def __repr__(self) -> str:
        return self.__str__()
