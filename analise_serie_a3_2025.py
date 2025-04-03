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
    times = ['Francana', 'Monte_Azul', 'Bandeirante', 'Catanduva', 'Comercial', 'Desportivo_Brasil', 'Lemense', 'EC_Sao_Bernardo', 'XV_de_Jau', 'Marilia', 'Rio_Branco', 'Rio_Preto', 'Sertaozinho', 'Itapirense', 'Uniao_Sao_Joao', 'Uniao_Suzano']
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
    pontuacao = {time: {'pontos': 0, 'vitorias': 0} for time in ['Francana', 'Monte_Azul', 'Bandeirante', 'Catanduva', 'Comercial', 'Desportivo_Brasil', 'Lemense', 'EC_Sao_Bernardo', 'XV_de_Jau', 'Marilia', 'Rio_Branco', 'Rio_Preto', 'Sertaozinho', 'Itapirense', 'Uniao_Sao_Joao', 'Uniao_Suzano']}
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
    lista_times = ['Francana', 'Monte_Azul', 'Bandeirante', 'Catanduva', 'Comercial', 'Desportivo_Brasil', 'Lemense', 'EC_Sao_Bernardo', 'XV_de_Jau', 'Marilia', 'Rio_Branco', 'Rio_Preto', 'Sertaozinho', 'Itapirense', 'Uniao_Sao_Joao', 'Uniao_Suzano']
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
    ['Uniao_Suzano 1x1 Uniao_Sao_Joao', 'Rio_Branco 3x1 EC_Sao_Bernardo', 'Rio_Preto 3x0 Catanduva', 'Itapirense 1x2 Monte_Azul', 'Lemense 0x0 Comercial', 'Francana 1x1 Sertaozinho', 'Bandeirante 2x1 Marilia', 'XV_de_Jau 0x0 Desportivo_Brasil'], # RODADA 1
    ['Comercial 0x1 Uniao_Suzano', 'Monte_Azul 1x1 Rio_Branco', 'EC_Sao_Bernardo 1x1 Francana', 'Uniao_Sao_Joao 0x0 XV_de_Jau', 'Sertaozinho 1x0 Lemense', 'Catanduva 2x0 Bandeirante', 'Marilia 1x0 Itapirense', 'Desportivo_Brasil 0x1 Rio_Preto'], # RODADA 2
    ['Uniao_Sao_Joao 0x1 Itapirense', 'Sertaozinho 0x1 Catanduva', 'Lemense 1x1 Uniao_Suzano', 'Marilia 2x0 Comercial', 'EC_Sao_Bernardo 0x1 XV_de_Jau', 'Rio_Branco 1x1 Rio_Preto', 'Monte_Azul 1x1 Desportivo_Brasil', 'Francana 4x2 Bandeirante'], # RODADA 3
    ['Desportivo_Brasil 1x2 Marilia', 'Rio_Preto 1x0 Comercial', 'Uniao_Suzano 0x2 Sertaozinho', 'XV_de_Jau 0x2 Rio_Branco', 'Itapirense 0x1 Lemense', 'Francana 1x1 Monte_Azul', 'Catanduva 1x0 EC_Sao_Bernardo', 'Bandeirante 0x1 Uniao_Sao_Joao'], # RODADA 4
    ['Comercial 1x3 Uniao_Sao_Joao', 'Sertaozinho 1x2 Rio_Branco', 'Catanduva 3x1 Uniao_Suzano', 'Lemense 1x1 Francana', 'Bandeirante 0x2 Itapirense', 'Marilia 2x1 XV_de_Jau', 'EC_Sao_Bernardo 1x0 Desportivo_Brasil', 'Monte_Azul 4x0 Rio_Preto'], # RODADA 5
    ['Rio_Branco 1x1 Francana', 'Rio_Preto 0x0 EC_Sao_Bernardo', 'Uniao_Suzano 1x3 Monte_Azul', 'Uniao_Sao_Joao 3x3 Desportivo_Brasil', 'Lemense 1x1 Marilia', 'XV_de_Jau 0x0 Bandeirante', 'Itapirense 0x1 Sertaozinho', 'Comercial 2x0 Catanduva'], # RODADA 6
    ['Uniao_Suzano 1x0 Rio_Preto', 'EC_Sao_Bernardo 1x0 Monte_Azul', 'Desportivo_Brasil 2x0 Comercial', 'Sertaozinho 1x0 XV_de_Jau', 'Catanduva 0x0 Rio_Branco', 'Marilia 2x1 Uniao_Sao_Joao', 'Francana 1x2 Itapirense', 'Bandeirante 1x0 Lemense'], # RODADA 7
    ['Marilia 3x1 EC_Sao_Bernardo', 'Desportivo_Brasil 1x0 Catanduva', 'Rio_Branco 4x0 Lemense', 'Rio_Preto 0x1 Francana', 'Uniao_Sao_Joao 0x1 Sertaozinho', 'Comercial 1x2 Itapirense', 'Monte_Azul 2x1 Bandeirante', 'XV_de_Jau 2x1 Uniao_Suzano'], # RODADA 8
    ['EC_Sao_Bernardo 1x1 Uniao_Sao_Joao', 'Uniao_Suzano 2x1 Marilia', 'Lemense 1x0 Rio_Preto', 'Itapirense 2x3 Desportivo_Brasil', 'Sertaozinho 1x1 Comercial', 'Francana 0x1 XV_de_Jau', 'Catanduva 1x1 Monte_Azul', 'Bandeirante 1x0 Rio_Branco'], # RODADA 9
    ['Desportivo_Brasil 0x2 Sertaozinho', 'EC_Sao_Bernardo 1x1 Bandeirante', 'Uniao_Sao_Joao 1x0 Rio_Branco', 'Comercial 1x1 Francana', 'Itapirense 2x0 Uniao_Suzano', 'Catanduva 3x2 Lemense', 'Monte_Azul 3x1 Marilia', 'XV_de_Jau 0x1 Rio_Preto'], # RODADA 10
    ['Monte_Azul 1x0 Comercial', 'Rio_Branco 2x3 Desportivo_Brasil', 'Rio_Preto 0x0 Itapirense', 'Lemense 1x0 XV_de_Jau', 'Sertaozinho 0x0 EC_Sao_Bernardo', 'Francana 2x1 Uniao_Sao_Joao', 'Marilia 3x1 Catanduva', 'Bandeirante 3x0 Uniao_Suzano'], # RODADA 11
    ['Uniao_Suzano 3x0 Francana', 'Desportivo_Brasil 2x1 Lemense', 'Rio_Preto 3x0 Bandeirante', 'Uniao_Sao_Joao 0x1 Monte_Azul', 'Comercial 0x0 EC_Sao_Bernardo', 'Itapirense 1x0 Rio_Branco', 'Catanduva 2x1 XV_de_Jau', 'Sertaozinho 0x0 Marilia'], # RODADA 12
    ['Rio_Branco 2x1 Uniao_Suzano', 'Monte_Azul 1x1 Sertaozinho', 'Desportivo_Brasil 1x1 Francana', 'EC_Sao_Bernardo 2x1 Lemense', 'Uniao_Sao_Joao 1x0 Catanduva', 'XV_de_Jau 1x0 Itapirense', 'Marilia 1x1 Rio_Preto', 'Comercial 2x0 Bandeirante'], # RODADA 13
    ['Uniao_Suzano 2x1 EC_Sao_Bernardo', 'Rio_Branco 4x0 Comercial', 'Rio_Preto 1x1 Sertaozinho', 'Itapirense 0x1 Catanduva', 'Lemense 0x1 Uniao_Sao_Joao', 'Francana 0x1 Marilia', 'XV_de_Jau 2x2 Monte_Azul', 'Bandeirante 0x1 Desportivo_Brasil'], # RODADA 14
    ['Monte_Azul 4x2 Lemense', 'Catanduva 2x2 Francana', 'Comercial 0x0 XV_de_Jau', 'Desportivo_Brasil 1x0 Uniao_Suzano', 'EC_Sao_Bernardo 1x1 Itapirense', 'Marilia 3x3 Rio_Branco', 'Sertaozinho 1x1 Bandeirante', 'Uniao_Sao_Joao 4x0 Rio_Preto'], # RODADA 15
]

rodadas_restantes = [
    # SEM JOGOS A SEREM DISPUTADOS
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
