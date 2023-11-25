class NodoHistoria:
    def __init__(self, texto, opcion_1=None, opcion_2=None):
        self.texto = texto
        self.opcion_1 = opcion_1
        self.opcion_2 = opcion_2

def jugar_historia(nodo_actual):
    print(nodo_actual.texto)

    decision = input("Que decides? (1/2): ")

    if decision == '1' and nodo_actual.opcion_1:
        jugar_historia(nodo_actual.opcion_1)
    elif decision == '2' and nodo_actual.opcion_2:
        jugar_historia(nodo_actual.opcion_2)
    else:
        print("Fin del juego!")

nodo1 = NodoHistoria("Eres un valiente caballero en busca de la princesa capturada. Tomar el camino del bosque oscuro (1) o el camino de la montana empinada (2)?")
nodo2 = NodoHistoria("Te adentras mas en el bosque y encuentras un rio. Buscar un puente (1) o nadar a traves de el (2)?")
nodo3 = NodoHistoria("Encuentras un puente, pero esta custodiado por un troll. Intentar persuadir al troll (1) o luchar contra el (2)?")
nodo4 = NodoHistoria("Has derrotado al troll. Ahora, decides continuar tu viaje. Ir a traves de la cueva misteriosa (1) o seguir el camino iluminado (2)?")
nodo5 = NodoHistoria("Dentro de la cueva, encuentras una bifurcacion. Tomar el camino de la izquierda (1) o el camino de la derecha (2)?")
nodo6 = NodoHistoria("Te encuentras con una encrucijada. Ir hacia la torre del mago (1) o explorar la cripta antigua (2)?")
nodo7 = NodoHistoria("Exploras la cripta antigua y encuentras un mapa antiguo. Confiar en tu instinto (1) o seguir el mapa (2)?")
nodo8 = NodoHistoria("Llegas a una puerta cerrada. Intentar abrir la puerta con fuerza (1) o buscar una llave (2)?")
nodo9 = NodoHistoria("Encuentras una llave en el suelo y abres la puerta. Has avanzado! Continuar hacia la sala del tesoro (1) o subir las escaleras (2)?")
nodo10 = NodoHistoria("Subes las escaleras y te enfrentas a un enemigo poderoso. Luchar contra el (1) o intentar negociar (2)?")
nodo11 = NodoHistoria("Felicidades! Has rescatado a la princesa y eres el heroe del reino :D.")
nodo12 = NodoHistoria("Oh no! Tu personaje ha muerto en la batalla :(.")
nodo13 = NodoHistoria("La princesa ha muerto :(.")

nodo1.opcion_1 = nodo2
nodo1.opcion_2 = nodo4
nodo2.opcion_1 = nodo3
nodo2.opcion_2 = nodo4
nodo3.opcion_1 = nodo5
nodo3.opcion_2 = nodo5
nodo4.opcion_1 = nodo6
nodo4.opcion_2 = nodo6
nodo5.opcion_1 = nodo7
nodo5.opcion_2 = nodo7
nodo6.opcion_1 = nodo7
nodo6.opcion_2 = nodo7
nodo7.opcion_1 = nodo8
nodo7.opcion_2 = nodo8
nodo8.opcion_1 = nodo9
nodo8.opcion_2 = nodo9
nodo9.opcion_1 = nodo10
nodo9.opcion_2 = nodo10
nodo10.opcion_1 = nodo11
nodo10.opcion_2 = nodo12
nodo11.opcion_1 = nodo13

jugar_historia(nodo1)