Gastos_João = [300, 500, 200, 800]
Gastos_Pedro = [200, 400, 500, 700]

Gastos_Mensais_João = sum(Gastos_João)
Gastos_Mensais_Pedro = sum(Gastos_Pedro)

if Gastos_Mensais_João > Gastos_Mensais_Pedro:
    print("João gastou mais que Pedro.")
else:
    print("Pedro gastou mais que João.")