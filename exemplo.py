import random

def simular_jogo(time1, time2):
    """Simula um jogo entre dois times, garantindo um vencedor ou empate."""
    resultado = random.random()
    if resultado < 0.45:  # 45% de chance para time1 vencer
        return time1
    elif resultado < 0.90:  # 45% de chance para time2 vencer
        return time2
    else:  # 10% de chance de empate
        return None


def simular_torneio(resultados_anteriores, rodadas_restantes):
    """Simula o restante do torneio, considerando os resultados anteriores e as rodadas restantes."""
    times = ['Vermelho_Escuro', 'Vermelho', 'Laranja', 'Amarelo', 'Verde_Claro', 'Verde', 'Azul_Claro', 'Azul', 'Azul_Escuro', 'Roxo']
    pontuacao = calcular_pontuacao(resultados_anteriores)

    for rodada in rodadas_restantes:
        for jogo in rodada:
            partes_jogo = jogo.split('x', 1)

            if len(partes_jogo) == 2:
                time1, time2 = partes_jogo

                time1 = time1.strip()  
                time2 = time2.strip()  

                vencedor = simular_jogo(time1, time2)

                if vencedor and vencedor in times:
                    pontuacao[vencedor] += 3
                else:  # Empate
                    if time1 in times and time2 in times:
                        pontuacao[time1] += 1
                        pontuacao[time2] += 1
    return pontuacao

def calcular_pontuacao(resultados):
    """Calcula a pontuação de cada time com base nos resultados dos jogos."""
    pontuacao = {'Vermelho_Escuro' : 0, 'Vermelho' : 0, 'Laranja' : 0, 'Amarelo' : 0, 'Verde_Claro' : 0, 'Verde' : 0, 'Azul_Claro' : 0, 'Azul' : 0, 'Azul_Escuro' : 0, 'Roxo' : 0}
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
    lista_times = ['Vermelho_Escuro', 'Vermelho', 'Laranja', 'Amarelo', 'Verde_Claro', 'Verde', 'Azul_Claro', 'Azul', 'Azul_Escuro', 'Roxo']  # Variável renomeada
    contagem_classificados = {time: 0 for time in lista_times}
    contagem_ultimos_ou_penultimos = {time: 0 for time in lista_times}

    for _ in range(num_simulacoes):
        pontuacao = simular_torneio(resultados_anteriores, rodadas_restantes)
        times_ordenados = sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)

        # Contagem para as oito primeiras posições, de onde sairão os classificados para a próxima fase
        for i in range(8):
            contagem_classificados[times_ordenados[i][0]] += 1

        # Contagem para as duas últimas posições, de onde sairão os rebaixados
        for i in range(len(lista_times) - 2, len(lista_times)):  
            contagem_ultimos_ou_penultimos[times_ordenados[i][0]] += 1

    probabilidades_classificados = {
        time: contagem / num_simulacoes for time, contagem in contagem_classificados.items()
    }

    probabilidades_ultimos_ou_penultimos = {
        time: contagem / num_simulacoes for time, contagem in contagem_ultimos_ou_penultimos.items()
    }

    return probabilidades_classificados, probabilidades_ultimos_ou_penultimos

# Exemplo de uso, 10 equipes jogando entre si para garantir 8 vagas para as quartas de final e os dois eliminados serão rebaixados ao fim destas 9 rodada (Campeonato de turno unico)
resultados_anteriores = [
    ['Vermelho_Escuro 1x6 Roxo', 'Vermelho 6x6 Azul_Escuro', 'Laranja 6x6 Azul', 'Amarelo 2x5 Azul_Claro', 'Verde_Claro 2x4 Verde'],#RODADA 1
    ['Vermelho_Escuro 4x5 Vermelho', 'Laranja 4x4 Roxo', 'Amarelo 4x3 Azul_Escuro', 'Verde_Claro 4x5 Azul', 'Verde 3x6 Azul_Claro'],#RODADA 2
    ['Vermelho_Escuro 6x1 Laranja', 'Amarelo 3x3 Vermelho', 'Verde_Claro 1x5 Roxo', 'Verde 1x5 Azul_Escuro', 'Azul 6x4 Azul_Claro'],#RODADA 3
    ['Vermelho_Escuro 2x6 Amarelo', 'Verde_Claro 2x2 Laranja', 'Verde 4x5 Vermelho', 'Azul_Claro 2x1 Roxo', 'Azul 1x6 Azul_Escuro'],#RODADA 4
    ['Vermelho_Escuro 3x6 Verde_Claro', 'Verde 6x6 Amarelo', 'Azul_Claro 5x1 Laranja', 'Azul 4x2 Vermelho', 'Azul_Escuro 6x3 Roxo'],#RODADA 5
]

rodadas_restantes = [
    ['Vermelho_Escuro x Verde', 'Azul_Claro x Verde_Claro', 'Azul x Amarelo', 'Azul_Escuro x Laranja', 'Roxo x Vermelho'],#RODADA 6
    ['Vermelho_Escuro x Azul_Claro', 'Azul x Verde', 'Azul_Escuro x Verde_Claro', 'Roxo x Amarelo', 'Vermelho x Laranja'],#RODADA 7
    ['Vermelho_Escuro x Azul', 'Azul_Escuro x Azul_Claro', 'Roxo x Verde', 'Vermelho x Verde_Claro', 'Laranja x Amarelo'],#RODADA 8
    ['Vermelho_Escuro x Azul_Escuro', 'Roxo x Azul', 'Vermelho x Azul_Claro', 'Laranja x Verde', 'Amarelo x Verde_Claro'],#RODADA 9
]

num_simulacoes = 1000  # Número de simulações para estimar as probabilidades

probabilidades_classificados, probabilidades_ultimos_ou_penultimos = calcular_probabilidades(num_simulacoes, resultados_anteriores, rodadas_restantes)
print("Probabilidades de classificacao para as quartas de final (8 vagas):")
for time, prob in probabilidades_classificados.items():  # Agora a variável está definida
    print(f"{time}: {prob:.2%}")

print("\nProbabilidades de ficar na zona de rebaixamento:")
for time, prob in probabilidades_ultimos_ou_penultimos.items():
    print(f"{time}: {prob:.2%}")
