class Nodo:
    def __init__(self, titulo, plataforma, año):
        self.titulo = titulo
        self.plataforma = plataforma
        self.año = año
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, titulo, plataforma, año):
        if not self.raiz:
            self.raiz = Nodo(titulo, plataforma, año)
        else:
            self._insertar_recursivo(titulo, plataforma, año, self.raiz)

    def _insertar_recursivo(self, titulo, plataforma, año, nodo_actual):
        if titulo < nodo_actual.titulo:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(titulo, plataforma, año)
            else:
                self._insertar_recursivo(titulo, plataforma, año, nodo_actual.izquierda)
        elif titulo > nodo_actual.titulo:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(titulo, plataforma, año)
            else:
                self._insertar_recursivo(titulo, plataforma, año, nodo_actual.derecha)
        else:
            pass

    def buscar(self, titulo):
        return self._buscar_recursivo(titulo, self.raiz)

    def _buscar_recursivo(self, titulo, nodo_actual):
        if nodo_actual is None or nodo_actual.titulo == titulo:
            return nodo_actual
        if titulo < nodo_actual.titulo:
            return self._buscar_recursivo(titulo, nodo_actual.izquierda)
        return self._buscar_recursivo(titulo, nodo_actual.derecha)

def imprimir_inorder(nodo):
    if nodo:
        imprimir_inorder(nodo.izquierda)
        print(f'Titulo: {nodo.titulo}, Plataforma: {nodo.plataforma}, Año: {nodo.año}')
        imprimir_inorder(nodo.derecha)

arbol_videojuegos = ArbolBinario()
arbol_videojuegos.insertar("The Legend of Zelda", "Nintendo Switch", 2017)
arbol_videojuegos.insertar("Super Mario Odyssey", "Nintendo Switch", 2017)
arbol_videojuegos.insertar("God of War", "PlayStation 4", 2018)
arbol_videojuegos.insertar("The Witcher 3", "Multiplataforma", 2015)

print("Arbol de videojuegos:")
imprimir_inorder(arbol_videojuegos.raiz)

# Busqueda binaria
juego_buscado = arbol_videojuegos.buscar("God of War")
if juego_buscado:
    print(f"\nJuego encontrado: {juego_buscado.titulo} ({juego_buscado.plataforma}, {juego_buscado.año})")
else:
    print("\nJuego no encontrado.")
