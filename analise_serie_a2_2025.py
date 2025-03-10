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
    times = ['Portuguesa_Santista', 'Capivariano', 'Juventus', 'Linense', 'Votuporanguense', 'Santo_Andre', 'Sao_Bento', 'Taubate', 'XV_de_Piracicaba', 'Ferroviaria', 'Gremio_Prudente', 'Ituano', 'Oeste', 'Primavera', 'Rio_Claro', 'Sao_Jose']
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
    pontuacao = {time: {'pontos': 0, 'vitorias': 0} for time in ['Portuguesa_Santista', 'Capivariano', 'Juventus', 'Linense', 'Votuporanguense', 'Santo_Andre', 'Sao_Bento', 'Taubate', 'XV_de_Piracicaba', 'Ferroviaria', 'Gremio_Prudente', 'Ituano', 'Oeste', 'Primavera', 'Rio_Claro', 'Sao_Jose']}
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
    lista_times = ['Portuguesa_Santista', 'Capivariano', 'Juventus', 'Linense', 'Votuporanguense', 'Santo_Andre', 'Sao_Bento', 'Taubate', 'XV_de_Piracicaba', 'Ferroviaria', 'Gremio_Prudente', 'Ituano', 'Oeste', 'Primavera', 'Rio_Claro', 'Sao_Jose']
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
    ['Oeste 1x2 XV_de_Piracicaba', 'Primavera 1x0 Sao_Bento', 'Taubate 1x2 Portuguesa_Santista', 'Capivariano 1x0 Santo_Andre', 'Linense 1x0 Juventus', 'Votuporanguense 0x2 Ferroviaria', 'Gremio_Prudente 2x0 Sao_Jose', 'Rio_Claro 1x1 Ituano'], # RODADA 1
    ['Santo_Andre 0x0 Primavera', 'Sao_Bento 0x0 Votuporanguense', 'XV_de_Piracicaba 2x0 Linense', 'Portuguesa_Santista 0x0 Capivariano', 'Juventus 2x2 Rio_Claro', 'Ituano 3x2 Gremio_Prudente', 'Sao_Jose 3x0 Taubate', 'Ferroviaria 0x1 Oeste'], # RODADA 2
    ['Juventus 3x1 Portuguesa_Santista', 'Santo_Andre 0x1 Taubate', 'Primavera 2x1 Linense', 'Rio_Claro 0x0 Sao_Jose', 'Capivariano 1x1 XV_de_Piracicaba', 'Ferroviaria 3x1 Ituano', 'Votuporanguense 0x2 Oeste', 'Gremio_Prudente 0x1 Sao_Bento'], # RODADA 3
    ['Capivariano 3x1 Ferroviaria', 'Taubate 2x0 Votuporanguense', 'Sao_Jose 0x0 Primavera', 'Ituano 1x0 Juventus', 'XV_de_Piracicaba 1x0 Gremio_Prudente', 'Portuguesa_Santista 0x2 Santo_Andre', 'Linense 1x1 Rio_Claro', 'Oeste 2x0 Sao_Bento'], # RODADA 4
    ['Juventus 2x3 Oeste', 'Santo_Andre 1x3 Votuporanguense', 'Rio_Claro 0x0 Capivariano', 'Ferroviaria 3x2 Taubate', 'Sao_Bento 0x0 Ituano', 'Gremio_Prudente 2x2 Primavera', 'Portuguesa_Santista 0x1 XV_de_Piracicaba', 'Sao_Jose 3x0 Linense'], # RODADA 5
    ['Primavera 3x1 Rio_Claro', 'Juventus 4x3 Ferroviaria', 'Ituano 1x1 Sao_Jose', 'Votuporanguense 2x1 Capivariano', 'Linense 2x0 Portuguesa_Santista', 'Oeste 0x3 Gremio_Prudente', 'Taubate 1x0 Sao_Bento', 'XV_de_Piracicaba 1x0 Santo_Andre'], # RODADA 6
    ['Santo_Andre 5x1 Rio_Claro', 'Oeste 2x2 Taubate', 'Capivariano 0x1 Gremio_Prudente', 'Ferroviaria 0x0 Primavera', 'Ituano 3x0 Linense', 'Sao_Bento 0x1 Portuguesa_Santista', 'XV_de_Piracicaba 0x1 Juventus', 'Sao_Jose 0x1 Votuporanguense'], # RODADA 7
    ['Taubate 0x2 Linense', 'Primavera 1x0 Oeste', 'Rio_Claro 2x3 XV_de_Piracicaba', 'Portuguesa_Santista 3x3 Ituano', 'Sao_Bento 0x5 Capivariano', 'Gremio_Prudente 2x2 Votuporanguense', 'Juventus 2x0 Sao_Jose', 'Ferroviaria 2x2 Santo_Andre'], # RODADA 8
    ['Oeste 0x0 Rio_Claro', 'Ituano 1x2 Primavera', 'Linense 2x2 Ferroviaria', 'Votuporanguense 1x1 Juventus', 'Portuguesa_Santista 0x2 Gremio_Prudente', 'Taubate 2x0 Capivariano', 'XV_de_Piracicaba 0x0 Sao_Bento', 'Sao_Jose 1x3 Santo_Andre'], # RODADA 9
    ['Capivariano 3x0 Oeste', 'Santo_Andre 2x2 Ituano', 'Primavera 2x1 Taubate', 'Rio_Claro 1x1 Portuguesa_Santista', 'Sao_Bento 3x2 Juventus', 'Gremio_Prudente 2x1 Linense', 'Votuporanguense 1x0 XV_de_Piracicaba', 'Ferroviaria 0x1 Sao_Jose'], # RODADA 10
    ['Juventus 1x1 Gremio_Prudente', 'Primavera 4x0 Votuporanguense', 'Ituano 0x0 Oeste', 'Linense 0x1 Capivariano', 'Sao_Bento 1x2 Santo_Andre', 'Taubate 2x1 Rio_Claro', 'XV_de_Piracicaba 1x2 Ferroviaria', 'Portuguesa_Santista 0x3 Sao_Jose'], # RODADA 11
    ['Oeste 1x0 Linense', 'Capivariano 1x0 Primavera', 'Santo_Andre 1x1 Juventus', 'Gremio_Prudente 1x2 Taubate', 'Votuporanguense 0x0 Rio_Claro', 'Sao_Jose 1x1 Sao_Bento', 'Ferroviaria 0x0 Portuguesa_Santista', 'XV_de_Piracicaba 0x0 Ituano'], # RODADA 12
    ['Juventus 2x2 Capivariano', 'Santo_Andre 0x0 Oeste', 'Rio_Claro 0x0 Gremio_Prudente', 'Ituano 1x0 Taubate', 'Sao_Bento 0x2 Ferroviaria', 'Portuguesa_Santista 0x0 Primavera', 'Sao_Jose 2x0 XV_de_Piracicaba', 'Linense 2x1 Votuporanguense'], # RODADA 13
    ['Linense 2x0 Sao_Bento', 'Votuporanguense 2x3 Ituano', 'Gremio_Prudente 0x0 Santo_Andre', 'Capivariano 1x0 Sao_Jose', 'Oeste 2x2 Portuguesa_Santista', 'Primavera 0x0 XV_de_Piracicaba', 'Rio_Claro 1x0 Ferroviaria', 'Taubate 0x0 Juventus'], # RODADA 14
    ['Portuguesa_Santista 0x0 Votuporanguense', 'Juventus 0x0 Primavera', 'Santo_Andre 3x1 Linense', 'Sao_Bento 3x0 Rio_Claro', 'XV_de_Piracicaba 1x3 Taubate', 'Ferroviaria 3x1 Gremio_Prudente', 'Ituano 3x0 Capivariano', 'Sao_Jose 1x0 Oeste'], # RODADA 15
]

rodadas_restantes = [
  #SEM JOGOS A SER DISPUTADOS
]

num_simulacoes = 1000  # Número de simulações para estimar as probabilidades

# ... (resto do código)

# Linha corrigida:
probabilidades_classificados, probabilidades_primeiros, probabilidades_ultimos_ou_penultimos = calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes)
print("Probabilidades apos o termino da 10 Rodada, Atualizado em 16/02/2025 as 19:40")
print("Probabilidades de classificacao para as quartas de final (8 vagas):")
for time, prob in probabilidades_classificados.items():  # Agora a variável está definida
    print(f"{time}: {prob:.2%}")

print("\nProbabilidades de ficar entre os quarto primeiros (4 vagas):")
for time, prob in probabilidades_primeiros.items():  # Agora a variável está definida
    print(f"{time}: {prob:.2%}")

print("\nProbabilidades de ficar na zona de rebaixamento para a Serie A3 de 2026:")
for time, prob in probabilidades_ultimos_ou_penultimos.items():
    print(f"{time}: {prob:.2%}")
    
print("\nProbabilidades de ficar na zona de rebaixamento para a Serie A3 de 2026:")
for time, prob in probabilidades_ultimos_ou_penultimos.items():
    print(f"{time}: {prob:.2%}")
