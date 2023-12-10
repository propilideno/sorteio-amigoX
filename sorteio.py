from random import shuffle

with open('pessoas.txt', 'r') as f:
# Read all lines of file, split by \n and ignore all empty lines
    pessoas = f.read().strip().split('\n')

shuffle(pessoas)
sorteio = {x:y for x, y in zip(pessoas, pessoas[1:] + pessoas[:1])}

print('=== Sorteio ===')
for k, v in sorteio.items():
    print(f'{k} tirou {v}')
