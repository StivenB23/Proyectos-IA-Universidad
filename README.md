# 🚌 Sistema Inteligente de Rutas del MIO (Cali)  
**Algoritmo de búsqueda de costo uniforme aplicado a transporte público**

---

## 📌 Descripción del Proyecto

Este proyecto simula una parte del sistema de transporte masivo de Cali, Colombia —el **MIO**— usando un modelo de **grafo no dirigido con pesos**, donde cada nodo representa una estación y cada arista representa una ruta directa entre estaciones, con un **peso asociado al tiempo estimado de viaje (en minutos)**.

Se utiliza el algoritmo de **Búsqueda de Costo Uniforme (Uniform Cost Search - UCS)** para encontrar la ruta óptima (es decir, de menor costo en tiempo) entre dos estaciones específicas.

Además, el grafo completo y la ruta óptima son visualizados gráficamente utilizando las librerías `networkx` y `matplotlib`.

---

## 🧠 ¿Qué es el MIO?

El **MIO** (Masivo Integrado de Occidente) es el sistema de transporte público de Cali, operado con buses articulados y estaciones de intercambio. Los usuarios se trasladan entre estaciones a través de rutas preestablecidas que varían en duración y conexiones.

---

## 🚏 Ejemplo de Estaciones y Rutas Modeladas

Se modelan estaciones conocidas de la ciudad como:

- `Paso_del_Comercio`
- `Chiminangos`
- `Salomia`
- `Flora_Industrial`
- `Alamos`
- `Popular`
- `Estadio`
- `Manzana_del_Saber`
- `Torre_de_Cali`

Y se representan rutas directas entre ellas como:

| Estación Origen       | Estación Destino       | Tiempo (min) |
|------------------------|-------------------------|----------------|
| Paso_del_Comercio      | Chiminangos             | 4              |
| Chiminangos            | Salomia                 | 3              |
| Salomia                | Flora_Industrial        | 5              |
| Flora_Industrial       | Alamos                  | 3              |
| Salomia                | Popular                 | 2              |
| Popular                | Estadio                 | 8              |
| Estadio                | Manzana_del_Saber       | 6              |
| ...                    | ...                     | ...            |

También se incluyen rutas alternativas y atajos para simular la complejidad del sistema.

---

## 🔍 Algoritmo Utilizado

### 🔹 Búsqueda de Costo Uniforme (UCS)

El algoritmo UCS es una variante de **Dijkstra**, utilizado cuando el costo para moverse entre nodos es variable (en este caso, tiempo).

### ¿Cómo funciona?

1. Se utiliza una **cola de prioridad** para explorar siempre el nodo con menor costo acumulado.
2. Se expande la ruta paso a paso, manteniendo la prioridad en el **menor tiempo total**.
3. Al llegar al destino, se devuelve la ruta óptima y el costo total.

Este enfoque garantiza encontrar la **ruta más eficiente** en términos de tiempo, sin importar la cantidad de transbordos.

---

## 🧰 Tecnologías y Librerías

| Herramienta       | Descripción                                      |
|-------------------|--------------------------------------------------|
| `Python`          | Lenguaje de programación principal               |
| `NetworkX`        | Modelado de grafos                               |
| `Matplotlib`      | Visualización del grafo                          |
| `heapq`           | Cola de prioridad para UCS                       |

### Instalación de dependencias

```bash
pip install networkx matplotlib
```

# Autores
Albert Ospina - John Hernandez