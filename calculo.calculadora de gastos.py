def calcular_total(gastos):
    return sum(gastos)

def calcular_promedio(gastos):
    if len(gastos) == 0:
        return 0
    return sum(gastos) / len(gastos)

def calcular_porcentaje(gastos_por_categoria, categoria):
    total = sum(gastos_por_categoria.values())
    if total == 0 or categoria not in gastos_por_categoria:
        return 0
    return (gastos_por_categoria[categoria] / total) * 100

# Parte de prueba (esto se ejecuta si corrés este archivo directamente)
if __name__ == "__main__":
    gastos = [1200, 3500, 890, 460]
    print("Total:", calcular_total(gastos))
    print("Promedio:", calcular_promedio(gastos))

    categorias = {
        "comida": 2500,
        "transporte": 1500,
        "alquiler": 5000
    }
    print("Porcentaje de comida:", calcular_porcentaje(categorias, "comida"), "%")
