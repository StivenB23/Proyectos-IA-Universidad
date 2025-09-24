import heapq
import networkx as nx
import matplotlib.pyplot as plt


def obtener_grafo_mio():
    """
    Define y retorna el grafo del sistema MIO con estaciones y tiempos.
    Esta función representa nuestra "base de conocimiento".
    """
    rutas_mio = [
        ('Paso_del_Comercio', 'Chiminangos', {'weight': 4}),
        ('Chiminangos', 'Salomia', {'weight': 3}),
        ('Salomia', 'Flora_Industrial', {'weight': 5}),
        ('Flora_Industrial', 'Alamos', {'weight': 3}),
        ('Salomia', 'Popular', {'weight': 2}),
        ('Popular', 'Estadio', {'weight': 8}),
        ('Estadio', 'Manzana_del_Saber', {'weight': 6}),
        ('Manzana_del_Saber', 'Alamos', {'weight': 10}),
        ('Chiminangos', 'Torre_de_Cali', {'weight': 12}),
        ('Torre_de_Cali', 'Alamos', {'weight': 7}),
        ('Paso_del_Comercio', 'Flora_Industrial', {'weight': 10}),
    ]

    grafo = nx.Graph()
    grafo.add_edges_from(rutas_mio)
    return grafo


def busqueda_costo_uniforme(graph, inicio, destino):
    """
    Encuentra la ruta de menor costo desde un nodo de inicio a uno de destino
    utilizando el algoritmo de Búsqueda de Costo Uniforme.
    """
    cola_prioridad = [(0, [inicio])]
    visitados = set()

    while cola_prioridad:
        costo, ruta = heapq.heappop(cola_prioridad)
        estacion_actual = ruta[-1]

        if estacion_actual in visitados:
            continue

        visitados.add(estacion_actual)

        if estacion_actual == destino:
            return ruta, costo

        for vecino, datos in graph[estacion_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + datos['weight']
                nueva_ruta = ruta + [vecino]
                heapq.heappush(cola_prioridad, (nuevo_costo, nueva_ruta))

    return None, float('inf')


def dibujar_grafo(graph, ruta_optima=None, inicio=None, destino=None):
    """
    Dibuja el grafo del sistema MIO, destacando la ruta óptima si se proporciona.
    """
    pos = nx.spring_layout(graph, seed=42, k=0.8)

    # Colores para nodos
    colores_nodos = []
    for nodo in graph.nodes():
        if nodo == inicio:
            colores_nodos.append('green')
        elif nodo == destino:
            colores_nodos.append('purple')
        elif ruta_optima and nodo in ruta_optima:
            colores_nodos.append('#ff6b6b')  # rojo suave
        else:
            colores_nodos.append('#00b4d8')  # azul cielo

    # Nodos
    nx.draw_networkx_nodes(graph, pos, node_size=1500, node_color=colores_nodos, edgecolors='black', linewidths=1.5)

    # Etiquetas de nodos
    etiquetas = {nodo: nodo.replace('_', ' ') for nodo in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels=etiquetas, font_size=10, font_weight='bold', font_color='black')

    # Aristas
    nx.draw_networkx_edges(graph, pos, width=2, alpha=0.4, edge_color='gray')

    # Pesos de aristas
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    edge_labels = {k: f"{v} min" for k, v in edge_labels.items()}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8, font_color='black')

    # Ruta óptima en rojo
    if ruta_optima:
        edges_ruta = list(zip(ruta_optima, ruta_optima[1:]))
        nx.draw_networkx_edges(graph, pos, edgelist=edges_ruta, edge_color='red', width=3)

    plt.title("Ruta Óptima en el Sistema MIO", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Inicializamos grafo
    grafo_mio = obtener_grafo_mio()
    estaciones_disponibles = sorted(list(grafo_mio.nodes()))

    print("\n🔄 Bienvenido al Sistema Inteligente de Rutas MIO")
    print("📍 Estaciones disponibles:\n")
    for i, est in enumerate(estaciones_disponibles, 1):
        print(f"{i}. {est.replace('_', ' ')}")
    
    # Solicitar entrada de usuario
    print("\n🔧 Ingrese los nombres exactos de la estación de origen y destino (use guiones bajos o copie):")
    estacion_inicio = input("🟢 Estación de Origen: ").strip()
    estacion_destino = input("🟣 Estación de Destino: ").strip()

    if estacion_inicio not in grafo_mio or estacion_destino not in grafo_mio:
        print("\n❌ Una o ambas estaciones no existen en la red. Intente de nuevo.")
    else:
        ruta_encontrada, costo_total = busqueda_costo_uniforme(grafo_mio, estacion_inicio, estacion_destino)

        print("\n🧠 Sistema Inteligente de Rutas MIO\n" + "=" * 45)
        if ruta_encontrada:
            print(f"📍 Estación de Origen:      {estacion_inicio.replace('_', ' ')}")
            print(f"🏁 Estación de Destino:     {estacion_destino.replace('_', ' ')}")
            print(f"🛣️  Ruta más corta:         {' -> '.join([r.replace('_', ' ') for r in ruta_encontrada])}")
            print(f"⏱️  Tiempo estimado total:  {costo_total} minutos")
        else:
            print("❌ No se encontró una ruta entre las estaciones seleccionadas.")

        dibujar_grafo(grafo_mio, ruta_optima=ruta_encontrada, inicio=estacion_inicio, destino=estacion_destino)
