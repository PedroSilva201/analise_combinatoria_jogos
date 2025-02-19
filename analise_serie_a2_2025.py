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
    times = ['Portuguesa_Santista', 'Capivariano', 'Juventus', 'Linense', 'Votuporanguense', 'Santo_Andre', 'Sao_Bento', 'Taubate', 'XV_de_Piracicaba', 'Ferroviaria', 'Gremio_Prudente', 'Ituano', 'Oeste', 'Primavera', 'Rio_Claro', 'Sao_Jose']
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
    pontuacao = {'Portuguesa_Santista': 0, 'Capivariano': 0, 'Juventus': 0, 'Linense': 0, 'Votuporanguense': 0, 'Santo_Andre': 0, 'Sao_Bento':0, 'Taubate':0, 'XV_de_Piracicaba':0, 'Ferroviaria':0, 'Gremio_Prudente':0, 'Ituano':0, 'Oeste':0, 'Primavera':0, 'Rio_Claro':0, 'Sao_Jose':0}
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
    lista_times = ['Portuguesa_Santista', 'Capivariano', 'Juventus', 'Linense', 'Votuporanguense', 'Santo_Andre', 'Sao_Bento', 'Taubate', 'XV_de_Piracicaba', 'Ferroviaria', 'Gremio_Prudente', 'Ituano', 'Oeste', 'Primavera', 'Rio_Claro', 'Sao_Jose']  # Variável renomeada
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
    ['Oeste 1x2 XV_de_Piracicaba', 'Primavera 1x0 Sao_Bento', 'Taubate 1x2 Portuguesa_Santista', 'Capivariano 1x0 Santo_Andre', 'Linense 1x0 Juventus', 'Votuporanguense 0x2 Ferroviaria', 'Gremio_Prudente 2x0 Sao_Jose', 'Rio_Claro 1x1 Ituano'],
    ['Santo_Andre 0x0 Primavera', 'Sao_Bento 0x0 Votuporanguense', 'XV_de_Piracicaba 2x0 Linense', 'Portuguesa_Santista 0x0 Capivariano', 'Juventus 2x2 Rio_Claro', 'Ituano 3x2 Gremio_Prudente', 'Sao_Jose 3x0 Taubate', 'Ferroviaria 0x1 Oeste'],
    ['Juventus 3x1 Portuguesa_Santista', 'Santo_Andre 0x1 Taubate', 'Primavera 2x1 Linense', 'Rio_Claro 0x0 Sao_Jose', 'Capivariano 1x1 XV_de_Piracicaba', 'Ferroviaria 3x1 Ituano', 'Votuporanguense 0x2 Oeste', 'Gremio_Prudente 0x1 Sao_Bento'],
    ['Capivariano 3x1 Ferroviaria', 'Taubate 2x0 Votuporanguense', 'Sao_Jose 0x0 Primavera', 'Ituano 1x0 Juventus', 'XV_de_Piracicaba 1x0 Gremio_Prudente', 'Portuguesa_Santista 0x2 Santo_Andre', 'Linense 1x1 Rio_Claro', 'Oeste 2x0 Sao_Bento'],
    ['Juventus 2x3 Oeste', 'Santo_Andre 1x3 Votuporanguense', 'Rio_Claro 0x0 Capivariano', 'Ferroviaria 3x2 Taubate', 'Sao_Bento 0x0 Ituano', 'Gremio_Prudente 2x2 Primavera', 'Portuguesa_Santista 0x1 XV_de_Piracicaba', 'Sao_Jose 3x0 Linense'],
    ['Primavera 3x1 Rio_Claro', 'Juventus 4x3 Ferroviaria', 'Ituano 1x1 Sao_Jose', 'Votuporanguense 2x1 Capivariano', 'Linense 2x0 Portuguesa_Santista', 'Oeste 0x3 Gremio_Prudente', 'Taubate 1x0 Sao_Bento', 'XV_de_Piracicaba 1x0 Santo_Andre'],
    ['Santo_Andre 5x1 Rio_Claro', 'Oeste 2x2 Taubate', 'Capivariano 0x1 Gremio_Prudente', 'Ferroviaria 0x0 Primavera', 'Ituano 3x0 Linense', 'Sao_Bento 0x1 Portuguesa_Santista', 'XV_de_Piracicaba 0x1 Juventus', 'Sao_Jose 0x1 Votuporanguense'],
    ['Taubate 0x2 Linense', 'Primavera 1x0 Oeste', 'Rio_Claro 2x3 XV_de_Piracicaba', 'Portuguesa_Santista 3x3 Ituano', 'Sao_Bento 0x5 Capivariano', 'Gremio_Prudente 2x2 Votuporanguense', 'Juventus 2x0 Sao_Jose', 'Ferroviaria 2x2 Santo_Andre'],
    ['Oeste 0x0 Rio_Claro', 'Ituano 1x2 Primavera', 'Linense 2x2 Ferroviaria', 'Votuporanguense 1x1 Juventus', 'Portuguesa_Santista 0x2 Gremio_Prudente', 'Taubate 2x0 Capivariano', 'XV_de_Piracicaba 0x0 Sao_Bento', 'Sao_Jose 1x3 Santo_Andre'],
    ['Capivariano 3x0 Oeste', 'Santo_Andre 2x2 Ituano', 'Primavera 2x1 Taubate', 'Rio_Claro 1x1 Portuguesa_Santista','Sao_Bento 3x2 Juventus', 'Gremio_Prudente 2x1 Linense', 'Votuporanguense 1x0 XV_de_Piracicaba', 'Ferroviaria 0x1 Sao_Jose'],
]

rodadas_restantes = [
    ['Juventus x Gremio_Prudente', 'Primavera x Votuporanguense', 'Ituano x Oeste', 'Linense x Capivariano', 'Sao_Bento x Santo_Andre', 'Taubate x Rio_Claro', 'XV_de_Piracicaba x Ferroviaria', 'Portuguesa_Santista x Sao_Jose'],
    ['Oeste x Linense', 'Capivariano x Primavera', 'Santo_Andre x Juventus', 'Gremio_Prudente x Taubate', 'Votuporanguense x Rio_Claro', 'Sao_Jose x Sao_Bento', 'Ferroviaria x Portuguesa_Santista', 'XV_de_Piracicaba x Ituano'],
    ['Juventus x Capivariano', 'Santo_Andre x Oeste', 'Rio_Claro x Gremio_Prudente', 'Ituano x Taubate', 'Sao_Bento x Ferroviaria', 'Portuguesa_Santista x Primavera', 'Sao_Jose x XV_de_Piracicaba', 'Linense x Votuporanguense'],
    ['Oeste x Portuguesa_Santista', 'Capivariano x Sao_Jose', 'Primavera x XV_de_Piracicaba', 'Rio_Claro x Ferroviaria', 'Gremio_Prudente x Santo_Andre', 'Votuporanguense x Ituano', 'Linense x Sao_Bento', 'Taubate x Juventus'],
    ['Portuguesa_Santista x Votuporanguense', 'Juventus x Primavera', 'Santo_Andre x Linense', 'Sao_Bento x Rio_Claro', 'XV_de_Piracicaba x Taubate', 'Ferroviaria x Gremio_Prudente', 'Ituano x Capivariano', 'Sao_Jose x Oeste']
]

num_simulacoes = 1000  # Número de simulações para estimar as probabilidades

# ... (resto do código)

# Linha corrigida:
probabilidades_classificados, probabilidades_ultimos_ou_penultimos = calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes)
print("Probabilidades apos o termino da 10 Rodada, Atualizado em 16/02/2025 as 19:40")
print("Probabilidades de classificacao para as quartas de final (8 vagas):")
for time, prob in probabilidades_classificados.items():  # Agora a variável está definida
    print(f"{time}: {prob:.2%}")
    
print("\nProbabilidades de ficar na zona de rebaixamento para a Serie A3 de 2026:")
for time, prob in probabilidades_ultimos_ou_penultimos.items():
    print(f"{time}: {prob:.2%}")
