import random

def simular_jogo(time1, time2):
  """Simula um jogo entre dois times, retornando o vencedor (ou None em caso de empate)."""
  if random.random() < 0.5:  # Assume 50% de chance de vitória para cada time
    return time1.strip()  # Remove espaços extras do time vencedor
  elif random.random() < 0.5:
    return time2.strip()  # Remove espaços extras do time vencedor
  else:
    return None  # Empate

def simular_torneio(resultados_anteriores, rodadas_restantes):
    """Simula o restante do torneio, considerando os resultados anteriores e as rodadas restantes."""
    times = ['Internacional_de_Bebedouro', 'Aracatuba', 'Barretos', 'Atletico_Joseense', 'Penapolense', 'Taquaritinga', 'Colorado_Caieras', 'Gremio_Sao_Carlense', 'Osasco', 'Jabaquara', 'Paulista', 'Nacional', 'Sao_Caetano', 'Matonense', 'Uniao_Barbarense', 'VOCEM']
    pontuacao = calcular_pontuacao(resultados_anteriores)

    for rodada in rodadas_restantes:
        for jogo in rodada:
            time1, time2 = jogo.split('x')
            vencedor = simular_jogo(time1, time2)
            if vencedor:
                pontuacao[vencedor] += 3
            else:  # Empate
                pontuacao[time1.strip()] += 1  # Remove espaços extras de time1
                pontuacao[time2.strip()] += 1  # Remove espaços extras de time2

    return pontuacao

def calcular_pontuacao(resultados):
    """Calcula a pontuação de cada time com base nos resultados dos jogos."""
    pontuacao = {'Internacional_de_Bebedouro': 0, 'Aracatuba': 0, 'Barretos': 0, 'Atletico_Joseense': 0, 'Penapolense': 0, 'Taquaritinga': 0, 'Colorado_Caieras': 0, 'Gremio_Sao_Carlense': 0, 'Osasco': 0, 'Jabaquara': 0, 'Paulista': 0, 'Nacional': 0, 'Sao_Caetano': 0, 'Matonense': 0, 'Uniao_Barbarense': 0, 'VOCEM': 0}
    for rodada in resultados:
        for jogo in rodada:
            partes = jogo.split(' ')
            time1 = partes[0].strip()  # Remove espaços extras de time1
            resultado = partes[1]
            placar1, placar2 = resultado.split('x')
            time2 = partes[2].strip()  # Remove espaços extras de time2

            if int(placar1) > int(placar2):
                pontuacao[time1] += 3
            elif int(placar1) == int(placar2):
                pontuacao[time1] += 1
                pontuacao[time2] += 1
            else:
                pontuacao[time2] += 3

    return pontuacao

def calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes):
    """Calcula a probabilidade de cada time terminar nas oito primeiras e duas últimas posições."""
    lista_times = ['Internacional_de_Bebedouro', 'Aracatuba', 'Barretos', 'Atletico_Joseense', 'Penapolense', 'Taquaritinga', 'Colorado_Caieras', 'Gremio_Sao_Carlense', 'Osasco', 'Jabaquara', 'Paulista', 'Nacional', 'Sao_Caetano', 'Matonense', 'Uniao_Barbarense', 'VOCEM']  # Variável renomeada
    contagem_classificados = {time: 0 for time in lista_times}
    contagem_ultimos_ou_penultimos = {time: 0 for time in lista_times}

    for _ in range(num_simulacoes):
        pontuacao = simular_torneio(resultados_anteriores, rodadas_restantes)
        times_ordenados = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)

        # Contagem para as duas primeiras posições
        for i in range(8):
            contagem_classificados[times_ordenados[i][0]] += 1

        # Contagem para as duas últimas posições
        for i in range(len(lista_times) - 2, len(lista_times)):  # Usando lista_times
            contagem_ultimos_ou_penultimos[times_ordenados[i][0]] += 1

    probabilidades_classificados = {
        time: contagem / num_simulacoes for time, contagem in contagem_classificados.items()
    }

    probabilidades_ultimos_ou_penultimos = {
        time: contagem / num_simulacoes for time, contagem in contagem_ultimos_ou_penultimos.items()
    }

    return probabilidades_classificados, probabilidades_ultimos_ou_penultimos

# Exemplo de uso
resultados_anteriores = [
    ['Atletico_Joseense 2x0 Taquaritinga', 'Colorado_Caieras 0x3 Barretos', 'Jabaquara 0x0 VOCEM', 'Nacional 1x2 Sao_Caetano', 'Penapolense 0x0 Uniao_Barbarense', 'Aracatuba 2x1 Gremio_Sao_Carlense', 'Internacional_de_Bebedouro 2x1 Osasco', 'Paulista 1x0 Matonense'],
    ['Taquaritinga 2x2 Colorado_Caieras', 'Sao_Caetano 0x1 Paulista', 'Osasco 0x2 Aracatuba', 'Gremio_Sao_Carlense 1x1 Atletico_Joseense', 'Barretos 2x0 Jabaquara', 'VOCEM 1x3 Penapolense', 'Matonense 0x3 Internacional_de_Bebedouro', 'Uniao_Barbarense 1x2 Nacional'],
    ['Taquaritinga 1x0 Nacional', 'Colorado_Caieras 0x2 Internacional_de_Bebedouro', 'Jabaquara 1x2 Uniao_Barbarense', 'Gremio_Sao_Carlense 3x3 Osasco', 'VOCEM 1x1 Barretos', 'Aracatuba 1x0 Matonense', 'Paulista 1x0 Penapolense', 'Sao_Caetano 2x1 Atletico_Joseense'],
    ['Nacional 2x0 Aracatuba', 'Internacional_de_Bebedouro 1x2 Jabaquara', 'Osasco 0x4 Paulista', 'Penapolense 1x1 Gremio_Sao_Carlense', 'Matonense 0x5 Colorado_Caieras', 'Uniao_Barbarense 2x4 Sao_Caetano', 'Atletico_Joseense 2x0 VOCEM', 'Barretos 1x3 Taquaritinga'],
    ['Taquaritinga 0x2 Uniao_Barbarense', 'Colorado_Caieras 3x1 Nacional', 'Jabaquara 1x1 Osasco', 'Paulista 1x0 Internacional_de_Bebedouro', 'Aracatuba 0x0 Barretos', 'Gremio_Sao_Carlense 2x0 Matonense', 'VOCEM 1x0 Sao_Caetano', 'Atletico_Joseense 3x1 Penapolense'],
    ['Jabaquara 0x1 Paulista', 'Matonense 0x4 Taquaritinga', 'Uniao_Barbarense 0x0 Atletico_Joseense', 'Penapolense 0x0 Colorado_Caieras', 'Internacional_de_Bebedouro 0x0 Nacional', 'Barretos 2x2 Gremio_Sao_Carlense', 'Osasco 1x1 VOCEM', 'Sao_Caetano 3x0 Aracatuba'],
    ['Taquaritinga 2x1 Internacional_de_Bebedouro', 'Colorado_Caieras 0x0 Atletico_Joseense', 'Nacional 1x0 Jabaquara', 'Paulista 1x3 Uniao_Barbarense', 'Aracatuba 0x0 Penapolense', 'Osasco 2x0 Barretos', 'VOCEM 0x2 Gremio_Sao_Carlense', 'Matonense 3x3 Sao_Caetano'],
]

rodadas_restantes = [
    ['Atletico_Joseense x Jabaquara', 'Taquaritinga x Osasco', 'Uniao_Barbarense x Matonense', 'Penapolense x Nacional', 'Gremio_Sao_Carlense x Internacional_de_Bebedouro', 'VOCEM x Aracatuba', 'Barretos x Paulista', 'Sao_Caetano x Colorado_Caieras'],
    ['Colorado_Caieras x Aracatuba', 'Jabaquara x Penapolense', 'Nacional x Barretos', 'Sao_Caetano x Taquaritinga', 'Internacional_de_Bebedouro x VOCEM', 'Osasco x Matonense', 'Paulista x Atletico_Joseense', 'Uniao_Barbarense x Gremio_Sao_Carlense'],
    ['Nacional x Paulista', 'Matonense x Atletico_Joseense', 'Penapolense x Taquaritinga', 'Gremio_Sao_Carlense x Jabaquara', 'VOCEM x Colorado_Caieras', 'Aracatuba x Internacional_de_Bebedouro', 'Barretos x Uniao_Barbarense', 'Osasco x Sao_Caetano'],
    ['Atletico_Joseense x Nacional', 'Taquaritinga x VOCEM', 'Jabaquara x Aracatuba', 'Paulista x Colorado_Caieras', 'Matonense x Barretos', 'Sao_Caetano x Gremio_Sao_Carlense', 'Internacional_de_Bebedouro x Penapolense', 'Uniao_Barbarense x Osasco'],
    ['Aracatuba x Paulista', 'Colorado_Caieras x Jabaquara', 'Nacional x Matonense', 'Internacional_de_Bebedouro x Atletico_Joseense', 'Gremio_Sao_Carlense x Taquaritinga', 'Barretos x Sao_Caetano', 'VOCEM x Uniao_Barbarense', 'Penapolense x Osasco'],
    ['Atletico_Joseense x Aracatuba', 'Taquaritinga x Paulista', 'Matonense x VOCEM', 'Uniao_Barbarense x Internacional_de_Bebedouro', 'Gremio_Sao_Carlense x Colorado_Caieras', 'Barretos x Penapolense', 'Osasco x Nacional', 'Sao_Caetano x Jabaquara'],
    ['Atletico_Joseense x Osasco', 'Colorado_Caieras x Uniao_Barbarense', 'Jabaquara x Matonense', 'Nacional x VOCEM', 'Paulista x Gremio_Sao_Carlense', 'Internacional_de_Bebedouro x Barretos', 'Aracatuba x Taquaritinga', 'Penapolense x Sao_Caetano'],
    ['Barretos x Atletico_Joseense', 'Taquaritinga x Jabaquara', 'Osasco x Colorado_Caieras', 'Gremio_Sao_Carlense x Nacional', 'Matonense x Penapolense', 'Sao_Caetano x Internacional_de_Bebedouro', 'Uniao_Barbarense x Aracatuba', 'VOCEM x Paulista'],
]

num_simulacoes = 1000  # Número de simulações para estimar as probabilidades

# ... (resto do código)

# Linha corrigida:
probabilidades_classificados, probabilidades_ultimos_ou_penultimos = calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes)
print("Probabilidades apos o termino da 8 Rodada, Atualizado em 17/02/2025 as 11:40")
print("Probabilidades de classificacao para as quartas de final (8 vagas):")
for time, prob in probabilidades_classificados.items():  # Agora a variável está definida
    print(f"{time}: {prob:.2%}")
    
print("\nProbabilidades de ficar na zona de rebaixamento para a Serie A4 de 2026:")
for time, prob in probabilidades_ultimos_ou_penultimos.items():
    print(f"{time}: {prob:.2%}")
