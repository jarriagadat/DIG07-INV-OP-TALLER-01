import pyomo.environ as pyo

def crear_modelo(nodos, arcos_dict, oferta_demanda_dict):
    """
    Formulación abstracta del modelo de flujo a costo mínimo en Pyomo.
    No contiene datos incrustados.
    """
    m = pyo.ConcreteModel()
    
    # Conjuntos
    m.N = pyo.Set(initialize=list(nodos))
    m.A = pyo.Set(initialize=list(arcos_dict.keys()), dimen=2)
    
    # Variables de decisión
    m.x = pyo.Var(
        m.A, 
        domain=pyo.NonNegativeReals,
        bounds=lambda m, i, j: (arcos_dict[(i, j)][1], arcos_dict[(i, j)][2])
    )
    
    # Función Objetivo: Minimizar costo total mensual
    m.obj = pyo.Objective(
        expr=sum(arcos_dict[a][0] * m.x[a] for a in m.A), 
        sense=pyo.minimize
    )
    
    # Restricciones de Conservación de Flujo
    def regla_balance(m, n):
        sale  = sum(m.x[i, j] for (i, j) in m.A if i == n)
        entra = sum(m.x[i, j] for (i, j) in m.A if j == n)
        
        # Desigualdad para absorber capacidad ociosa en oferta
        if oferta_demanda_dict[n] > 0:
            return sale - entra <= oferta_demanda_dict[n]
        # Igualdad estricta en demandas y transbordos
        else:
            return sale - entra == oferta_demanda_dict[n]
            
    m.bal = pyo.Constraint(m.N, rule=regla_balance)
    
    # Exportación de precios sombra (valores duales)
    m.dual = pyo.Suffix(direction=pyo.Suffix.IMPORT)
    
    return m