from random import choice

pessoas = ['João', 'Maria', 'José', 'Pedro']
tamanhoSorteio = len(pessoas)
sorteio = dict()

while len(sorteio) < tamanhoSorteio:
    sorteador = pessoas.pop(0)
    sorteado = choice(list(sorteio.keys()) + pessoas)
    print('Pessoas', pessoas)
    print('Sorteio', sorteio)
    while sorteado in sorteio.values():
        sorteado = choice(list(sorteio.keys()) + pessoas)
    sorteio[sorteador] = sorteado

print('Resultado do sorteio:')
for k, v in sorteio.items():
    print(f'{k} tirou {v}')
