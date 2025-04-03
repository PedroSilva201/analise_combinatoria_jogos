import random

def simular_jogo(time1, time2):
    """Simula um jogo entre dois times, retornando o vencedor (ou None em caso de empate)."""
    if random.random() < 0.5:
        return time1.strip()
    elif random.random() < 0.5:
        return time2.strip()
    else:
        return None

def simular_torneio(resultados_anteriores, rodadas_restantes):
    """Simula o restante do torneio, considerando os resultados anteriores e as rodadas restantes."""
    times = ['Internacional_de_Bebedouro', 'Aracatuba', 'Barretos', 'Atletico_Joseense', 'Penapolense', 'Taquaritinga', 'Colorado_Caieras', 'Gremio_Sao_Carlense', 'Osasco', 'Jabaquara', 'Paulista', 'Nacional', 'Sao_Caetano', 'Matonense', 'Uniao_Barbarense', 'VOCEM']
    pontuacao = calcular_pontuacao(resultados_anteriores)

    for rodada in rodadas_restantes:
        for jogo in rodada:
            time1, time2 = jogo.split('x')
            vencedor = simular_jogo(time1, time2)
            if vencedor:
                pontuacao[vencedor]['pontos'] += 3
                pontuacao[vencedor]['vitorias'] += 1
            else:
                pontuacao[time1.strip()]['pontos'] += 1
                pontuacao[time2.strip()]['pontos'] += 1

    return pontuacao

def calcular_pontuacao(resultados):
    """Calcula a pontuação e o número de vitórias de cada time com base nos resultados dos jogos."""
    pontuacao = {time: {'pontos': 0, 'vitorias': 0} for time in ['Internacional_de_Bebedouro', 'Aracatuba', 'Barretos', 'Atletico_Joseense', 'Penapolense', 'Taquaritinga', 'Colorado_Caieras', 'Gremio_Sao_Carlense', 'Osasco', 'Jabaquara', 'Paulista', 'Nacional', 'Sao_Caetano', 'Matonense', 'Uniao_Barbarense', 'VOCEM']}
    for rodada in resultados:
        for jogo in rodada:
            partes = jogo.split(' ')
            time1 = partes[0].strip()
            resultado = partes[1]
            placar1, placar2 = resultado.split('x')
            time2 = partes[2].strip()

            if int(placar1) > int(placar2):
                pontuacao[time1]['pontos'] += 3
                pontuacao[time1]['vitorias'] += 1
            elif int(placar1) == int(placar2):
                pontuacao[time1]['pontos'] += 1
                pontuacao[time2]['pontos'] += 1
            else:
                pontuacao[time2]['pontos'] += 3
                pontuacao[time2]['vitorias'] += 1

    return pontuacao

def calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes):
    """Calcula a probabilidade de cada time terminar nas oito primeiras e duas últimas posições."""
    lista_times = ['Internacional_de_Bebedouro', 'Aracatuba', 'Barretos', 'Atletico_Joseense', 'Penapolense', 'Taquaritinga', 'Colorado_Caieras', 'Gremio_Sao_Carlense', 'Osasco', 'Jabaquara', 'Paulista', 'Nacional', 'Sao_Caetano', 'Matonense', 'Uniao_Barbarense', 'VOCEM']
    contagem_classificados = {time: 0 for time in lista_times}
    contagem_primeiros = {time: 0 for time in lista_times}
    contagem_ultimos_ou_penultimos = {time: 0 for time in lista_times}

    for _ in range(num_simulacoes):
        pontuacao = simular_torneio(resultados_anteriores, rodadas_restantes)
        times_ordenados = sorted(pontuacao.items(), key=lambda x: (x[1]['vitorias'], x[1]['pontos']), reverse=True)

        for i in range(8):
            contagem_classificados[times_ordenados[i][0]] += 1

        for i in range(4):
            contagem_primeiros[times_ordenados[i][0]] += 1

        for i in range(len(lista_times) - 2, len(lista_times)):
            contagem_ultimos_ou_penultimos[times_ordenados[i][0]] += 1

    probabilidades_classificados = {time: contagem / num_simulacoes for time, contagem in contagem_classificados.items()}
    probabilidades_primeiros = {time: contagem / num_simulacoes for time, contagem in contagem_primeiros.items()}
    probabilidades_ultimos_ou_penultimos = {time: contagem / num_simulacoes for time, contagem in contagem_ultimos_ou_penultimos.items()}

    return probabilidades_classificados, probabilidades_primeiros, probabilidades_ultimos_ou_penultimos

# Exemplo de uso

# Exemplo de uso
resultados_anteriores = [
    ['Atletico_Joseense 2x0 Taquaritinga', 'Colorado_Caieras 0x3 Barretos', 'Jabaquara 0x0 VOCEM', 'Nacional 1x2 Sao_Caetano', 'Penapolense 0x0 Uniao_Barbarense', 'Aracatuba 2x1 Gremio_Sao_Carlense', 'Internacional_de_Bebedouro 2x1 Osasco', 'Paulista 1x0 Matonense'],# RODADA 1
    ['Taquaritinga 2x2 Colorado_Caieras', 'Sao_Caetano 0x1 Paulista', 'Osasco 0x2 Aracatuba', 'Gremio_Sao_Carlense 1x1 Atletico_Joseense', 'Barretos 2x0 Jabaquara', 'VOCEM 1x3 Penapolense', 'Matonense 0x3 Internacional_de_Bebedouro', 'Uniao_Barbarense 1x2 Nacional'],# RODADA 2
    ['Taquaritinga 1x0 Nacional', 'Colorado_Caieras 0x2 Internacional_de_Bebedouro', 'Jabaquara 1x2 Uniao_Barbarense', 'Gremio_Sao_Carlense 3x3 Osasco', 'VOCEM 1x1 Barretos', 'Aracatuba 1x0 Matonense', 'Paulista 1x0 Penapolense', 'Sao_Caetano 2x1 Atletico_Joseense'],# RODADA 3
    ['Nacional 2x0 Aracatuba', 'Internacional_de_Bebedouro 1x2 Jabaquara', 'Osasco 0x4 Paulista', 'Penapolense 1x1 Gremio_Sao_Carlense', 'Matonense 0x5 Colorado_Caieras', 'Uniao_Barbarense 2x4 Sao_Caetano', 'Atletico_Joseense 2x0 VOCEM', 'Barretos 1x3 Taquaritinga'],# RODADA 4
    ['Taquaritinga 0x2 Uniao_Barbarense', 'Colorado_Caieras 3x1 Nacional', 'Jabaquara 1x1 Osasco', 'Paulista 1x0 Internacional_de_Bebedouro', 'Aracatuba 0x0 Barretos', 'Gremio_Sao_Carlense 2x0 Matonense', 'VOCEM 1x0 Sao_Caetano', 'Atletico_Joseense 3x1 Penapolense'],# RODADA 5
    ['Jabaquara 0x1 Paulista', 'Matonense 0x4 Taquaritinga', 'Uniao_Barbarense 0x0 Atletico_Joseense', 'Penapolense 0x0 Colorado_Caieras', 'Internacional_de_Bebedouro 0x0 Nacional', 'Barretos 2x2 Gremio_Sao_Carlense', 'Osasco 1x1 VOCEM', 'Sao_Caetano 3x0 Aracatuba'],# RODADA 6
    ['Taquaritinga 2x1 Internacional_de_Bebedouro', 'Colorado_Caieras 0x0 Atletico_Joseense', 'Nacional 1x0 Jabaquara', 'Paulista 1x3 Uniao_Barbarense', 'Aracatuba 0x0 Penapolense', 'Osasco 2x0 Barretos', 'VOCEM 0x2 Gremio_Sao_Carlense', 'Matonense 3x3 Sao_Caetano'],# RODADA 7
    ['Atletico_Joseense 1x0 Jabaquara', 'Taquaritinga 0x0 Osasco', 'Uniao_Barbarense 3x0 Matonense', 'Penapolense 0x3 Nacional', 'Gremio_Sao_Carlense 1x1 Internacional_de_Bebedouro', 'VOCEM 1x2 Aracatuba', 'Barretos 0x0 Paulista', 'Sao_Caetano 2x2 Colorado_Caieras'],# RODADA 8
    ['Colorado_Caieras 2x0 Aracatuba', 'Jabaquara 2x1 Penapolense', 'Nacional 0x0 Barretos', 'Sao_Caetano 1x0 Taquaritinga', 'Internacional_de_Bebedouro 1x1 VOCEM', 'Osasco 3x2 Matonense', 'Paulista 1x0 Atletico_Joseense', 'Uniao_Barbarense 1x0 Gremio_Sao_Carlense'],# RODADA 9
    ['Nacional 1x0 Paulista', 'Matonense 1x2 Atletico_Joseense', 'Penapolense 1x2 Taquaritinga', 'VOCEM 3x3 Colorado_Caieras', 'Aracatuba 0x3 Internacional_de_Bebedouro', 'Barretos 1x3 Uniao_Barbarense', 'Osasco 1x3 Sao_Caetano', 'Gremio_Sao_Carlense 0x1 Jabaquara'],# RODADA 10
    ['Atletico_Joseense 2x2 Nacional', 'Jabaquara 0x1 Aracatuba', 'Paulista 3x5 Colorado_Caieras', 'Matonense 2x3 Barretos', 'Sao_Caetano 2x1 Gremio_Sao_Carlense', 'Internacional_de_Bebedouro 1x1 Penapolense', 'Taquaritinga 2x0 VOCEM', 'Uniao_Barbarense 3x0 Osasco'],# RODADA 11
    ['Aracatuba 0x0 Paulista', 'Colorado_Caieras 2x0 Jabaquara', 'Nacional 3x2 Matonense', 'Internacional_de_Bebedouro 1x1 Atletico_Joseense', 'Gremio_Sao_Carlense 1x2 Taquaritinga', 'Barretos 0x0 Sao_Caetano', 'VOCEM 2x1 Uniao_Barbarense', 'Penapolense 2x2 Osasco'],# RODADA 12
    ['Matonense 2x3 VOCEM', 'Atletico_Joseense 0x2 Aracatuba', 'Taquaritinga 0x0 Paulista', 'Uniao_Barbarense 2x0 Internacional_de_Bebedouro', 'Gremio_Sao_Carlense 1x1 Colorado_Caieras', 'Barretos 0x2 Penapolense', 'Osasco 0x2 Nacional', 'Sao_Caetano 0x1 Jabaquara'],# RODADA 13
    ['Atletico_Joseense 3x0 Osasco', 'Colorado_Caieras 0x2 Uniao_Barbarense', 'Jabaquara 3x1 Matonense', 'Nacional 0x3 VOCEM', 'Paulista 0x0 Gremio_Sao_Carlense',  'Aracatuba 3x1 Taquaritinga', 'Penapolense 1x1 Sao_Caetano','Internacional_de_Bebedouro 3x1 Barretos'],# RODADA 14
    ['Barretos 0x1 Atletico_Joseense', 'Taquaritinga 2x1 Jabaquara', 'Osasco 1x3 Colorado_Caieras', 'Gremio_Sao_Carlense 0x0 Nacional', 'Matonense 0x3 Penapolense', 'Sao_Caetano 2x2 Internacional_de_Bebedouro', 'Uniao_Barbarense 3x0 Aracatuba', 'VOCEM 1x1 Paulista'],# RODADA 15
]

rodadas_restantes = [
    #SEM JOGOS A SEREM REALIZADOS
]


num_simulacoes = 1000  # Número de simulações para estimar as probabilidades

# ... (resto do código)

# Linha corrigida:
probabilidades_classificados, probabilidades_primeiros, probabilidades_ultimos_ou_penultimos = calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes)
print("Probabilidades apos o termino da 10 Rodada, Atualizado em 16/02/2025 as 19:40")
print("Probabilidades de classificacao para as quartas de final (8 vagas):")
for time, prob in probabilidades_classificados.items():  # Agora a variável está definida
    print(f"{time}: {prob:.2%}")

print("\nProbabilidades de ficar na zona de rebaixamento para a Serie B de 2026:")
for time, prob in probabilidades_ultimos_ou_penultimos.items():
    print(f"{time}: {prob:.2%}")
