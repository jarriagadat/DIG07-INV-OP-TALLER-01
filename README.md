# Taller 1: Formulación y Optimización de Red de Flujo a Costo Mínimo
**Programa:** Doctorado en Ingeniería (UV–UTA)  
**Asignatura:** DIG07 Investigación de Operaciones
Profesor: Schulze, E.
**Fecha:** Septiembre 2026

## Descripción del Proyecto

Este repositorio contiene la solución para el problema de optimización de la red de logística minera. El objetivo principal es determinar el plan de despacho mensual de mínimo costo desde las faenas concentradoras hasta los puertos de exportación, transitando por acopios intermedios.

El modelo está formulado como un Problema de Flujo a Costo Mínimo (Min-Cost Network Flow) implementado en Pyomo y resuelto mediante HiGHS.


## Cómo ejecutar

## Integrantes
+ Pasmiño, Catherinne
+ Jara, Felipe
+ Arriagada, Jorge

## Instancia asignada
+ Minería

# Estructura del repositorio
Taller1__/ \
├── README.md cómo ejecutar, integrantes, instancia asignada \
├── datos/ los CSV entregados, sin modificar \
├── modelo.py formulación en Pyomo, sin datos incrustados \
├── resultados/ \
│ ├── solucion.csv flujos óptimos arco por arco \
│ └── duales.csv valores duales de los nodos \
└──cuaderno.ipynb desarrollo, verificación y respuestas \

___

🛠️ Requisitos Previos e Instalación
Para ejecutar este proyecto de forma limpia, asegúrate de contar con Python 3.10+ y los siguientes paquetes:

Bash
pip install pyomo pandas numpy matplotlib highs

🚀 Instrucciones de Ejecución
Opción 1: Ejecución Interactiva (Recomendada)
Abre el cuaderno cuaderno.ipynb en tu entorno de Jupyter Notebook o VS Code:

Bash
jupyter notebook cuaderno.ipynb
Ejecuta las celdas en secuencia (Run All). El cuaderno cargará los datos desde datos/, ejecutará las verificaciones de balance de masa, calculará los determinantes de unimodularidad total, resolverá el modelo y exportará las salidas automáticamente a la carpeta resultados/.

Opción 2: Uso Modular de modelo.py
Para integrar el modelo en scripts automatizados, puedes importar la función generadora desde Python:


