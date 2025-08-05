# Apresentação do Projeto

Este projeto consiste na montagem de um programa que analisa os resultados das partidas de futebol, podendo ser adaptado ao numero de participantes bem como o numero de jogos que cada equipe terá e as rodadas de um campeonato, podendo ser aplicado em exemplos da vida real.

## Análise combinatória de jogos

Em competições esportivas das mais variadas modalidades, sobretudo no futebol é muito comum os calculos de probabilidade para que uma equipe tenha determinadas chances de conseguir uma classificação ou eliminação de determinado campeonato, mas para isso é necessario entender que nem sempre todos os campeonatos são disputados em pontos corridos ou no sistema de todos contra todos bem como as copas não são disputados exclusivamente no formato eliminatório, o popular "mata-mata", em alguns casos quando não se enquadra nenhum ou nem outro é considerado sistema misto.

A mesma coisa ocorre quando é determinado a queda de uma equipe para uma divisão inferior, tecnicamente demininado de "Sistema de Ligas" onde é constituido uma serie de campeonatos disputados simultaneamente ao longo de uma determinada temporada onde os melhores obtem a acensão para um nivel superior e os piores para ocupar as vagas de quem acabou subindo, demininado de promoção e despromoção ou acesso e rebaixamento.

Com isso foi utilizado um exemplo ficticio de um campeonato com as seguintes equipes:

Vermelho Escuro
Vermelho
Laranja
Amarelo
Verde Claro
Verde
Azul Claro
Azul
Azul Escuro
Roxo
Todos os dez participantes jogam entre si em 9 (nove) rodadas e ao final do mesmo os oito primeiros se classificam para a próxima fase, supondo que fosse as quartas de final, e os dois piores, neste caso os eliminados seriam rebaixados para o grupo inferior, ao decorrer da disputa na medida dos jogos forem ocorrendo a tabela acaba sendo atualizada e tambem as combinações com base em um cenario de jogos a serem disputados com base em uma serie de fatores como o emparelhamento das rodadas, os jogos como mandante, as partidas demininadas de "confronto direto" e entre outros.

Para a simulação dos resultados foi utilizado um dado de 6 (seis) faces para anotar os cenarios dos jogos a serem dispitados com base o que foi explicado acima, no exemplo foi anotado os resultados da 5 rodada em diante:

Análise ao termino da 5ª rodada

![Image](https://github.com/user-attachments/assets/35994dc1-fc45-46c3-a71f-61ecf781e069)

Análise ao termino da 6ª rodada

![Image](https://github.com/user-attachments/assets/e3bfd753-ced0-492f-b120-5738cc270223)

Análise ao termino da 7ª rodada

![Image](https://github.com/user-attachments/assets/aa1dce73-7f03-4339-82fd-aa793af77894)

Análise ao termino da 8ª rodada

![Image](https://github.com/user-attachments/assets/5271447b-4b41-4190-a8a5-cd93534b34d8)

Análise ao termino da 9ª rodada

![Image](https://github.com/user-attachments/assets/617ba377-b540-4126-8f3f-66766d54a038)

Detalhes do código:

![Image](https://github.com/user-attachments/assets/5bb1f0df-dd94-43ad-b76f-3870f7e71e24)

No segundo for existe uma funcionalidade que calcula o numero de vagas nas posições superiores, neste exemplo é utilizado o numero 8, podendo ser qualuqer um como exemplo os numeros 2, 4 ou 6.

Da mesma forma que no for seguinte que calcula quem está nas posições inferiores, sobretudo na zona de rebaixamento, o numero neste caso é 2, mas pode ser 1, 3 ou 4 por exemplo.

No caso das funções times, pontuação e lista_times, sendo que o primeiro e o ultimo são identicos, no caso da pontuação é aceescido :0 para efeito dos calculos no inicio, neste exemplo utiliza-se dez equipes, podendo ser usado 12, 14 ou 16

Aqui tambem será dispobilizados códigos das tabelas das divisões inferiores do Campeonato Paulista de 2025, das series A2, A3 e A4, respectivamnete, segunda, terceira e quarta divisão estadual com os jogos para a realização dos calculos de probabilidade.

Creditos: a grande parte do código foi gerado pelo Gemini e alguns elementos pelo Chat GPT e em alguns casos foi utilizado de forma manual, criando ou copiando tabelas geradas na internt como neste site <a href="https://tabelas.fiatjaf.com/"> Do Gerador de tabelas de todos contra todos</a> por exemplo, no caso do exemplo das cores fiz de forma manual devido ao dominio que tenho por anos.

Para aprofundar mais sobre o conteúdo tem estes artigos da Wikípedia:

<a href="https://pt.wikipedia.org/wiki/Campe%C3%A3o">Campeão</a>

<a href="https://pt.wikipedia.org/wiki/Campeonato">Campeonato</a>

<a href="https://pt.wikipedia.org/wiki/Competi%C3%A7%C3%A3o_esportiva">Competição Esportiva</a>

<a href="https://pt.wikipedia.org/wiki/Competi%C3%A7%C3%B5es_de_todos_contra_todos">Competições de Todos Contra Todos</a>

<a href="https://pt.wikipedia.org/wiki/Competi%C3%A7%C3%B5es_eliminat%C3%B3rias">Competições Eliminatórias</a>

<a href="https://pt.wikipedia.org/wiki/Competi%C3%A7%C3%B5es_mistas">Competições Mistas</a>

<a href="https://pt.wikipedia.org/wiki/Promo%C3%A7%C3%A3o_e_Despromo%C3%A7%C3%A3o">Promoção e Despormoção</a>

## Pontos Importantes
No caso da probabilidade é calculado o numero de vagas vezes 100 (N*100) diante dos cenarios em que o mesmo disponha, tanto para as primeiras posições, como para as ultimas, caso se houver bagas intermediarias o certame tambem será aplicado, futuramente isso será demonstrado aqui.

No caso do Osasco Audax, o mesmo está representado com o nome de Osasco apenas para evitar o porblema de conflito com o x minusculo do nome em relação ao mesmo caractere correspondente do confronto, mas se for X maiusculo o sistema entende por completo.

O mesmo poderá ser rodado em qualquer plataformas de desenvolvimento como o Virtual Studio Code e o Pycharm, além do Colab se for em nuvem.
