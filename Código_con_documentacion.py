# NOTA:

# Mano yo siempre uso el interprete de visual studio code para que sepa, y yo instale una libreria para lo del grafo, la libreria es la siguiente : pip install networkx matplotlib



import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Parte 1: Base de Conocimiento (Reglas Lógicas representadas como un Grafo)
# Representamos el sistema MIO como un grafo donde las estaciones son nodos
# y las rutas son aristas con un 'peso' que es el tiempo estimado de viaje en minutos.

# Ruta: Desde 'Paso del Comercio' hasta 'Alamos' (cerca de Chipichape)
# Los datos de tiempo son estimaciones basadas en la información de rutas del MIO.
# (Estación_Origen, Estación_Destino, {'weight': tiempo_en_minutos})

def obtener_grafo_mio():
    """
    Define y retorna el grafo del sistema MIO con estaciones y tiempos.
    Esta función representa nuestra "base de conocimiento".
    """
    # Creamos una lista de aristas que representan las conexiones y sus costos (tiempo)
    # Incluimos varias rutas posibles para que el algoritmo pueda elegir.
    rutas_mio = [
        # Ruta principal (similar a la T31)
        ('Paso_del_Comercio', 'Chiminangos', {'weight': 4}),
        ('Chiminangos', 'Salomia', {'weight': 3}),
        ('Salomia', 'Flora_Industrial', {'weight': 5}),
        ('Flora_Industrial', 'Alamos', {'weight': 3}),

        # Ruta alternativa 1 (conexión en Salomia)
        ('Salomia', 'Popular', {'weight': 2}),
        ('Popular', 'Estadio', {'weight': 8}), # Ruta más larga para probar el algoritmo
        ('Estadio', 'Manzana_del_Saber', {'weight': 6}),
        ('Manzana_del_Saber', 'Alamos', {'weight': 10}), # Conexión poco óptima

        # Ruta alternativa 2 (Transbordo en Chiminangos con otra ruta)
        ('Chiminangos', 'Torre_de_Cali', {'weight': 12}), # Ruta que se desvía
        ('Torre_de_Cali', 'Alamos', {'weight': 7}),

        # Atajo o ruta expresa que conecta dos puntos no consecutivos
        ('Paso_del_Comercio', 'Flora_Industrial', {'weight': 10})
    ]
    
    # Creamos el grafo usando la librería NetworkX
    G = nx.Graph()
    G.add_edges_from(rutas_mio)
    return G

# Parte 2: Algoritmo de Búsqueda de Costo Uniforme (UCS)
def busqueda_costo_uniforme(graph, inicio, destino):
    """
    Encuentra la ruta de menor costo desde un nodo de inicio a uno de destino
    utilizando el algoritmo de Búsqueda de Costo Uniforme.
    """
    # La cola de prioridad almacenará tuplas de (costo_acumulado, ruta_actual)
    # Empezamos con un costo de 0 en la estación de inicio.
    cola_prioridad = [(0, [inicio])]
    
    # Un conjunto para guardar las estaciones que ya hemos visitado con la ruta más corta
    visitados = set()

    while cola_prioridad:
        # Extraemos la ruta con el MENOR costo acumulado gracias a heapq
        (costo, ruta) = heapq.heappop(cola_prioridad)
        
        # Obtenemos la última estación de la ruta actual
        estacion_actual = ruta[-1]

        # Si ya hemos encontrado la ruta más corta a esta estación, la ignoramos
        if estacion_actual in visitados:
            continue
        
        # Marcamos la estación actual como visitada
        visitados.add(estacion_actual)

        # ¡Hemos llegado al destino! Devolvemos la ruta y el costo final.
        if estacion_actual == destino:
            return ruta, costo

        # Exploramos las estaciones vecinas (conexiones directas)
        # El grafo de networkx nos da los vecinos y los datos de la arista (el peso)
        for vecino, datos in graph[estacion_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + datos['weight']
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                # Agregamos la nueva ruta a la cola de prioridad para ser evaluada
                heapq.heappush(cola_prioridad, (nuevo_costo, nueva_ruta))
    
    # Si el bucle termina y no encontramos el destino, no hay ruta
    return None, float('inf')

# Parte 3: Función para generar y mostrar el grafo
def dibujar_grafo(graph, ruta_optima=None):
    """
    Dibuja el grafo del sistema MIO, destacando la ruta óptima si se proporciona.
    """
    # Posicionamiento de los nodos para una mejor visualización
    pos = nx.spring_layout(graph, seed=42)
    
    # Dibujamos los nodos y las etiquetas
    nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color='skyblue')
    nx.draw_networkx_labels(graph, pos, font_size=8, font_weight='bold')
    
    # Dibujamos las aristas (rutas)
    nx.draw_networkx_edges(graph, pos, width=2, alpha=0.5, edge_color='gray')
    
    # Añadimos las etiquetas de peso (tiempo) a cada arista
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Si encontramos una ruta óptima, la resaltamos en color rojo
    if ruta_optima:
        edges_ruta = list(zip(ruta_optima, ruta_optima[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges_ruta, edge_color='red', width=3)
    
    plt.title("Grafo del Sistema MIO: Paso del Comercio a Alamos")
    plt.axis('off') # Ocultamos los ejes
    plt.show()


# Parte 4: Ejecución principal del programa
if __name__ == "__main__":
    # Definimos el problema
    grafo_mio = obtener_grafo_mio()
    estacion_inicio = 'Paso_del_Comercio'
    estacion_destino = 'Manzana_del_Saber' # Estación más cercana a Chipichape

    # Ejecutamos el algoritmo de búsqueda
    ruta_encontrada, costo_total = busqueda_costo_uniforme(grafo_mio, estacion_inicio, estacion_destino)

    # Mostramos los resultados
    print("--- Sistema Inteligente de Rutas MIO ---")
    if ruta_encontrada:
        print(f"📍 Estación de Origen: {estacion_inicio}")
        print(f"🏁 Estación de Destino: {estacion_destino}")
        print("-" * 35)
        print(f"✅ La mejor ruta encontrada es:")
        print(" -> ".join(ruta_encontrada))
        print(f"\n⏱️  Costo total (tiempo estimado): {costo_total} minutos.")
    else:
        print(f"❌ No se encontró una ruta desde {estacion_inicio} hasta {estacion_destino}.")

    # Generamos la visualización del grafo con la ruta resaltada
    dibujar_grafo(grafo_mio, ruta_encontrada)
