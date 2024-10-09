prev_ant = 0
ant = 1
resul = 0

print(prev_ant)
print(ant)

while resul < 100:
    resul = ant + prev_ant
    prev_ant = ant
    ant = resul

    print(resul)
