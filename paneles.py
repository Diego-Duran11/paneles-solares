# Permitir al usuario introducir sus propios valores
consumo_anual = float(input("Ingrese el consumo anual de energía en kWh: "))
horas_sol = float(input("Ingrese las horas promedio de sol por día: "))
eficiencia_panel = float(input("Ingrese la eficiencia del panel en %: ")) / 100
area_panel = float(input("Ingrese el área del panel en metros cuadrados: "))
radiacion_solar = float(input("Ingrese la radiación solar promedio en kWh/m²/día: "))

potencia_diaria_panel = area_panel * radiacion_solar * eficiencia_panel

potencia_anual_panel = potencia_diaria_panel * 365

num_paneles = consumo_anual / potencia_anual_panel

num_paneles = round(num_paneles)

area_total = num_paneles * area_panel

# Resultados
print(f"Número de paneles necesarios: {num_paneles}")
print(f"Área total necesaria para instalar los paneles: {area_total} m²")