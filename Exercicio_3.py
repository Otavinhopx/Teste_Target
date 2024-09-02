#Não havia arquivo xml ou json no teste, portanto eu gerei valores aleatórios

faturamento_mensal = {"dia 1": 12.500, "dia 2":14.200, "dia 3":13.800, "dia 4":15.000, "dia 5":14.500, "dia 6":16.000, "dia 7":15.500, "dia 8":16.300,
                      "dia 9":14.400, "dia 10":17.000, "dia 11":16.800, "dia 12":16.100, "dia 13":18.500, "dia 14":19.200, "dia 15":15.900,
                      "dia 16":11.400, "dia 17":13.600, "dia 18":17.700, "dia 19":16.700, "dia 20":14.800, "dia 21":19.200, "dia 22":10.800,
                      "dia 23":10.500, "dia 24":12.500, "dia 25":12.700, "dia 27":14.800, "dia 27":18.000, "dia 28":16.400, "dia 29":16.000, "dia 30":15.600,}

faturamento_mensal_maior={}

minimo = min(faturamento_mensal, key=faturamento_mensal.get)
maximo = max(faturamento_mensal, key=faturamento_mensal.get)
media = sum(faturamento_mensal.values()) / len(faturamento_mensal)

for valor in faturamento_mensal:
    if faturamento_mensal > media:
        faturamento_mensal_maior.append(valor)

print("Valor minimo foi no", minimo)
print("Valor máximo foi no", maximo)
print("Dias acima da média:")
print(faturamento_mensal_maior)