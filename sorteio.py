from random import shuffle

pessoas = ['João', 'Maria', 'José', 'Pedro']
shuffle(pessoas)
sorteio = {x:y for x, y in zip(pessoas, pessoas[1:] + pessoas[:1])}

print('Sorteio: ')
for k, v in sorteio.items():
    print(f'{k} tirou {v}')
