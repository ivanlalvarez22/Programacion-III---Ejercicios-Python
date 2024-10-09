lista_notas = [10, 11, 5, -1, 6, 8, 9, 2, 1, 0, 3]

resultados = list(map(lambda nota: "Aprobado" if nota >= 6 and nota <= 10 else (
    "Desaprobado" if nota >= 0 and nota <= 5 else "Nota inválida"), lista_notas))


print(resultados)
