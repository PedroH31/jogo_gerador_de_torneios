numero_de_times = int(input('Digite o número de times no torneio: '))
lista_de_times = []
vitorias_por_time = {}
numero_de_jogos = 0

while numero_de_times < 2:
    if numero_de_times < 2:
        print('O número mínimo de times é 2, tente de novo.')

    numero_de_times = int(input('Digite o número de times no torneio: '))

numero_do_time = 1

while len(lista_de_times) < numero_de_times:

    time = input(f'Digite o nome do time #{numero_do_time}: ')
    if time.count(' ') > 1:
        print('Nomes de time devem ter no máximo 2 palavras, tente de novo.')

    elif len(time) < 2:
        print('Nomes de time devem ter pelo menos 2 caracteres, tente de novo.')

    else:
        lista_de_times.append(time)
        numero_do_time += 1

while True:
    numero_de_jogos = int(input('Digite o número de jogos a serem jogados por cada time: '))
    if numero_de_jogos < len(lista_de_times) - 1:
        print('Número inválido de jogos. Cada time deve jogar um contra o outro pelo menos uma vez, tente de novo.')

    else:
        break

indice = 0

while len(vitorias_por_time) < len(lista_de_times):
    time_na_lista = lista_de_times[indice]
    numero_de_vitorias = int(input(f'Digite o número de vitórias do time {time_na_lista}: '))

    if numero_de_vitorias < 0:
        print('O número mínimo de vitórias é 0, tente de novo.')

    elif numero_de_vitorias > numero_de_jogos:
        print(f'O número de vitórias máximo é {numero_de_jogos}, tente de novo.')

    else:
        vitorias_por_time[time_na_lista] = numero_de_vitorias
        indice += 1

print('Gerando os jogos a serem jogados no primeiro round do torneio...')

pareamento = []

for time, vitorias in vitorias_por_time.items():
    pareamento.append((time, vitorias))
    sorted(pareamento, key=lambda vitoria: vitoria[1])

casa = -1
fora = 0
for time in pareamento:
    print(f'Casa: {pareamento[casa]} VS Fora: {pareamento[fora]}')
    casa -= 1
    fora += 1
    if fora == len(pareamento) / 2:
        break

