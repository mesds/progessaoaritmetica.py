print('Gerador de PA')
print('-= '* 10)
primeiro = int(input('Primeiro termo'))
razão = int(input('Razão de PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo))
    termo += razão
    cont += 1
print('FIM')
