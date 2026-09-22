km=float(input())
fuel_consumption=float(input())
cost_1l=float(input())
fuel=(km/100)*fuel_consumption
cost= fuel*cost_1l
print(print(f"Топливо: {fuel:.2f} л"))
print(f"Стоимость: {cost:.2f} руб")