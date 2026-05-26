from typing import Any, List
from collections import deque

class GrafoMatriz:

  def __init__(self):
    self.matrizAdy : List[List[int]] = []
    self.vertices : List[Any] = [] ## Lista con los nodos
    self.tamano : int = 0

  def agregarVertice(self, valor: any): ## Agrega el nodo pero desconectado
    if valor in self.vertices: ## Si el valor ya estaba agregado no hace nada mas
      return None
    self.vertices.append(valor) ## Agrega el vertice a lista de vertices
    self.tamano = self.tamano + 1 ## Incrementa el tamaño del grafo

    for fila in self.matrizAdy:
      fila.append(0) ## Agrega una fila de ceros
    self.matrizAdy.append([0] * self.tamano) ## Agrega una columna de ceros

  def agregarConexion(self, vertice1, vertice2, dirigido = False, peso = 1):
    if vertice1 not in self.vertices:
      self.agregarVertice(vertice1)
    if vertice2 not in self.vertices:
      self.agregarVertice(vertice2)

    posV1 = self.vertices.index(vertice1) ## Entrega la posicion de el vertice 1 en la matriz de ady
    posV2 = self.vertices.index(vertice2) ## Entrega la posicion del vertice 2 en la matriz de adyacencia

    self.matrizAdy[posV1][posV2] = peso ## Hay un camino entre v1 y v2

    if not dirigido: ## Si no es dirigido debo agregar la relacion contraria
      self.matrizAdy[posV2][posV1] = peso

  def recorrerEnAnchura ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.vertices: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    cola = deque([verticeInicial])  ## Cola de pendientes por visitar
    while cola:  ## Mientras que tenga vertices pendientes por visitar
      vertice = cola.popleft()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        posicionVertice = self.vertices.index(vertice)  ## Obtengo la fila dentro de la matriz en la cual debo buscar los vecinos
        for i in range(self.tamano):  ## Recorrer la matriz ady para buscar vertices relacionados
          if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados: ## Si encuentro un vertice relacionado y que no ha sido visitado
            cola.append(self.vertices[i])  ## Agrego ese vertice a la cola de pendientes por visitar
    return visitados

  def recorrerEnProfundidad( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.vertices: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    pila = [verticeInicial]  ## Pila de pendientes por visitar
    while pila:  ## Mientras que tenga vertices pendientes por visitar
      vertice = pila.pop()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        posicionVertice = self.vertices.index(vertice)  ## Obtengo la fila dentro de la matriz en la cual debo buscar los vecinos
        for i in range(self.tamano - 1, -1, -1):  ## Recorrer la matriz ady para buscar vertices relacionados (Se recorre en sentio inverso)
          if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados: ## Si encuentro un vertice relacionado y que no ha sido visitado
            pila.append(self.vertices[i])  ## Agrego ese vertice a la cola de pendientes por visitar
    return visitados


  def encontrarCaminoMasCorto(self, verticeInicial : Any, verticeFinal : Any) -> tuple:
    if verticeInicial not in self.vertices or verticeFinal not in self.vertices:
      ## Si alguno de los 2 vertices no existe
      return (float('inf'), [])

    ## Crea un diccionario donde inicalmente todas las distancias son infinitas
    distancias = { vertice : float('inf') for vertice in self.vertices }
    ## La distancia al vertice inicial es la unica que se conoce con antelacion
    distancias[verticeInicial] = 0

    ## Crea un diccionario donde inicalmente todas las distancias son infinitas
    predecesores = { vertice : None for vertice in self.vertices }

    visitados = [] ## Lista donde almacenaremos los vertices cuando los hayamos visitado

    verticeActual = verticeInicial

    ## Mientras que el vertice actual sea un nodo valido y sea diferente al vertice final
    while verticeActual is not None and verticeActual != verticeFinal:
      ## Consultar todos los vecinos del vertice actual que no he visitado
      vecinosNoVisitados = []
      posicionVertice = self.vertices.index(verticeActual)
      for i in range(self.tamano):
        if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados:
          vecinosNoVisitados.append(self.vertices[i])
      ## Actualizar los recorridos de la mejor ruta conocida
      for vecino in vecinosNoVisitados:
        ## Busca en la matriz de ady el peso de la conexion entre el vertice actual y el vecino no visitado
        pesoConexion = self.matrizAdy[posicionVertice][self.vertices.index(vecino)]
        ## acumula la mejor distancia conocida con la conexion actual
        distancia = distancias[verticeActual] + pesoConexion
        ## Si encontre una distancia menor a la que tenia registrada como mejor distancia conocida
        if distancia < distancias[vecino]:
          distancias[vecino] = distancia ## Actualizo mi nueva mejor distancia
          predecesores[vecino] = verticeActual ## Actualizo que la mejor distancia se dio con este predecesor
      visitados.append(verticeActual)

      distanciaMenor = float('inf')
      verticeMenor = None

      for vertice in distancias:
        if distancias[vertice] < distanciaMenor and vertice not in visitados:
          distanciaMenor = distancias[vertice]
          verticeMenor = vertice

      verticeActual = verticeMenor
    caminoMasCorto = []

    if distancias[verticeFinal] == float('inf'):
      return(float('inf'), [])

    pasoActual = verticeFinal

    while pasoActual is not None:
      caminoMasCorto.insert(0, pasoActual)
      pasoActual = predecesores[pasoActual]
    return (distancias[verticeFinal], caminoMasCorto)

  def arbolExpansionMinimo(self) -> tuple:
    if self.tamano == 0:
      return (0, []) ## Si el grafo esta vacio entonces no hay un AEM posible}

    verticesVisitados = [ self.vertices[0] ] ## Empiezo visitando el primer vertice del grafo segun su aparicion en la matriz
    conexionesArbol = [] ## Lista con todas las conexiones que hacen parte del arbol
    pesoTotal = 0 ## Acumular la longitud del AEM

    while len(verticesVisitados) < self.tamano: ## La cantidad de vertices visitados
      pesoMasBajo = float('inf')
      origenElegido = None
      destinoElegido = None

      ## Buscar todos los vecinos no visitados de los nodos del AEM
      for vertice in verticesVisitados: ## Para cada vertice en los vertices visitados
        indiceFila = self.vertices.index(vertice) ## Consultamos la fila en la cual debemos buscar los vecinos

        for indice in range(self.tamano): ## Recorremos la fila desde la posicion inicial hasta el final
          verticeEvaluado = self.vertices[indice]
          pesoEvaluado = self.matrizAdy[indiceFila][indice]

          if pesoEvaluado != 0 and verticeEvaluado not in verticesVisitados: ## Validamos que el V Evaluado sea un vecino y que ademas no haya sido visitado
            if pesoEvaluado < pesoMasBajo: ## Si el vecino evaluado es el mejor vecino hasta el momento
              pesoMasBajo = pesoEvaluado
              origenElegido = vertice
              destinoElegido = verticeEvaluado
      verticesVisitados.append(destinoElegido) ## Como en destino elegido me quedo el mejor vecino entonces lo visito
      conexionesArbol.append((origenElegido,destinoElegido, pesoMasBajo))
      pesoTotal = pesoTotal + pesoMasBajo

    return (pesoTotal, conexionesArbol)
  def obtenerVecinos(self, vertice):
    if vertice not in self.vertices:
      return []
    posicion = self.vertices.index(vertice)
    vecinos = []
    for i in range(self.tamano):
      if self.matrizAdy[posicion][i] != 0:
        vecinos.append(self.vertices[i])
    return vecinos

  def obtenerArista(self, vertice1, vertice2):
    if vertice1 not in self.vertices or vertice2 not in self.vertices:
      return None
    pos1 = self.vertices.index(vertice1)
    pos2 = self.vertices.index(vertice2)
    peso = self.matrizAdy[pos1][pos2]
    if peso == 0:
      return None
    return type('Arista', (), {'distancia': peso, 'es_transitable': lambda self: True})()
