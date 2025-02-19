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
    times = ['Francana', 'Monte_Azul', 'Bandeirante', 'Catanduva', 'Comercial', 'Desportivo_Brasil', 'Lemense', 'EC_Sao_Bernardo', 'XV_de_Jau', 'Marilia', 'Rio_Branco', 'Rio_Preto', 'Sertaozinho', 'Itapirense', 'Uniao_Sao_Joao', 'Uniao_Suzano']
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
    pontuacao = {'Francana': 0, 'Monte_Azul': 0, 'Bandeirante': 0, 'Catanduva': 0, 'Comercial': 0, 'Desportivo_Brasil': 0, 'Lemense': 0, 'EC_Sao_Bernardo': 0, 'XV_de_Jau': 0, 'Marilia': 0, 'Rio_Branco': 0, 'Rio_Preto': 0, 'Sertaozinho': 0, 'Itapirense': 0, 'Uniao_Sao_Joao': 0, 'Uniao_Suzano': 0}
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
    lista_times = ['Francana', 'Monte_Azul', 'Bandeirante', 'Catanduva', 'Comercial', 'Desportivo_Brasil', 'Lemense', 'EC_Sao_Bernardo', 'XV_de_Jau', 'Marilia', 'Rio_Branco', 'Rio_Preto', 'Sertaozinho', 'Itapirense', 'Uniao_Sao_Joao', 'Uniao_Suzano']  # Variável renomeada
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
    ['Uniao_Suzano 1x1 Uniao_Sao_Joao', 'Rio_Branco 3x1 EC_Sao_Bernardo', 'Rio_Preto 3x0 Catanduva', 'Itapirense 1x2 Monte_Azul', 'Lemense 0x0 Comercial', 'Francana 1x1 Sertaozinho', 'Bandeirante 2x1 Marilia', 'XV_de_Jau 0x0 Desportivo_Brasil'],
    ['Comercial 0x1 Uniao_Suzano', 'Monte_Azul 1x1 Rio_Branco', 'EC_Sao_Bernardo 1x1 Francana', 'Uniao_Sao_Joao 0x0 XV_de_Jau', 'Sertaozinho 1x0 Lemense', 'Catanduva 2x0 Bandeirante', 'Marilia 1x0 Itapirense', 'Desportivo_Brasil 0x1 Rio_Preto'],
    ['Uniao_Sao_Joao 0x1 Itapirense', 'Sertaozinho 0x1 Catanduva', 'Lemense 1x1 Uniao_Suzano', 'Marilia 2x0 Comercial', 'EC_Sao_Bernardo 0x1 XV_de_Jau', 'Rio_Branco 1x1 Rio_Preto', 'Monte_Azul 1x1 Desportivo_Brasil', 'Francana 4x2 Bandeirante'],
    ['Desportivo_Brasil 1x2 Marilia', 'Rio_Preto 1x0 Comercial', 'Uniao_Suzano 0x2 Sertaozinho', 'XV_de_Jau 0x2 Rio_Branco', 'Itapirense 0x1 Lemense', 'Francana 1x1 Monte_Azul', 'Catanduva 1x0 EC_Sao_Bernardo', 'Bandeirante 0x1 Uniao_Sao_Joao'],
    ['Comercial 1x3 Uniao_Sao_Joao', 'Sertaozinho 1x2 Rio_Branco', 'Catanduva 3x1 Uniao_Suzano', 'Lemense 1x1 Francana', 'Bandeirante 0x2 Itapirense', 'Marilia 2x1 XV_de_Jau', 'EC_Sao_Bernardo 1x0 Desportivo_Brasil', 'Monte_Azul 4x0 Rio_Preto'],
    ['Rio_Branco 1x1 Francana', 'Rio_Preto 0x0 EC_Sao_Bernardo', 'Uniao_Suzano 1x3 Monte_Azul', 'Uniao_Sao_Joao 3x3 Desportivo_Brasil', 'Lemense 1x1 Marilia', 'XV_de_Jau 0x0 Bandeirante', 'Itapirense 0x1 Sertaozinho', 'Comercial 2x0 Catanduva'],
    ['Uniao_Suzano 1x0 Rio_Preto', 'EC_Sao_Bernardo 1x0 Monte_Azul', 'Desportivo_Brasil 2x0 Comercial', 'Sertaozinho 1x0 XV_de_Jau', 'Catanduva 0x0 Rio_Branco', 'Marilia 2x1 Uniao_Sao_Joao', 'Francana 1x2 Itapirense', 'Bandeirante 1x0 Lemense'],
    ['Marilia 3x1 EC_Sao_Bernardo', 'Desportivo_Brasil 1x0 Catanduva', 'Rio_Branco 4x0 Lemense', 'Rio_Preto 0x1 Francana', 'Uniao_Sao_Joao 0x1 Sertaozinho', 'Comercial 1x2 Itapirense', 'Monte_Azul 2x1 Bandeirante'],
]

rodadas_restantes = [
    ['XV_de_Jau x Uniao_Suzano'],
    ['EC_Sao_Bernardo x Uniao_Sao_Joao', 'Uniao_Suzano x Marilia', 'Lemense x Rio_Preto', 'Itapirense x Desportivo_Brasil', 'Sertaozinho x Comercial', 'Francana x XV_de_Jau', 'Catanduva x Monte_Azul', 'Bandeirante x Rio_Branco'],
    ['Desportivo_Brasil x Sertaozinho', 'EC_Sao_Bernardo x Bandeirante', 'Uniao_Sao_Joao x Rio_Branco', 'Comercial x Francana', 'Itapirense x Uniao_Suzano', 'Catanduva x Lemense', 'Monte_Azul x Marilia', 'XV_de_Jau x Rio_Preto'],
    ['Monte_Azul x Comercial', 'Rio_Branco x Desportivo_Brasil', 'Rio_Preto x Itapirense', 'Lemense x XV_de_Jau', 'Sertaozinho x EC_Sao_Bernardo', 'Francana x Uniao_Sao_Joao', 'Marilia x Catanduva', 'Bandeirante x Uniao_Suzano'],
    ['Uniao_Suzano x Francana', 'Desportivo_Brasil x Lemense', 'Rio_Preto x Bandeirante', 'Uniao_Sao_Joao x Monte_Azul', 'Comercial x EC_Sao_Bernardo', 'Itapirense x Rio_Branco', 'Catanduva x XV_de_Jau', 'Sertaozinho x Marilia'],
    ['Rio_Branco x Uniao_Suzano', 'Monte_Azul x Sertaozinho', 'Desportivo_Brasil x Francana', 'EC_Sao_Bernardo x Lemense', 'Uniao_Sao_Joao x Catanduva', 'XV_de_Jau x Itapirense', 'Marilia x Rio_Preto', 'Comercial x Bandeirante'],
    ['Uniao_Suzano x EC_Sao_Bernardo', 'Rio_Branco x Comercial', 'Rio_Preto x Sertaozinho', 'Itapirense x Catanduva', 'Lemense x Uniao_Sao_Joao', 'Francana x Marilia', 'XV_de_Jau x Monte_Azul', 'Bandeirante x Desportivo_Brasil'],
    ['Monte_Azul x Lemense', 'Catanduva x Francana', 'Comercial x XV_de_Jau', 'Desportivo_Brasil x Uniao_Suzano', 'EC_Sao_Bernardo x Itapirense', 'Marilia x Rio_Branco', 'Sertaozinho x Bandeirante', 'Uniao_Sao_Joao x Rio_Preto'],
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
