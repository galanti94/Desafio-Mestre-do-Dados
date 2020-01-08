from listas_especificas import somente_nome, somente_nascimento, somente_formacao
from escreve_arquivos import escrever_arquivo_csv
from plotando_gráficos import plotar

lista_nomes = somente_nome('usuario_nome_nascimento_formacao.csv')
lista_nascimento = somente_nascimento('usuario_nome_nascimento_formacao.csv')
lista_formacao = somente_formacao('usuario_nome_nascimento_formacao.csv')
tamanho_lista_nomes = len(lista_nomes)

nomes = []
datas = []
formacao = []

contagem_nomes = []
contagem_datas = []
contagem_formacao = []

for i in range(0, tamanho_lista_nomes):
    contador_nomes = 0
    contador_datas = 0
    contador_formacao = 0

    if lista_nomes[i] not in nomes:
        for j in range(0, tamanho_lista_nomes):
            if lista_nomes[i] == lista_nomes[j]:
                contador_nomes += 1
    if lista_nascimento[i] not in datas:
        for j in range(0, tamanho_lista_nomes):
            if lista_nascimento[i] == lista_nascimento[j]:
                contador_datas += 1
    if lista_formacao[i] not in formacao:
        for j in range(0, tamanho_lista_nomes):
            if lista_formacao[i] == lista_formacao[j]:
                contador_formacao += 1

    if contador_nomes > 1:
        nomes.append(lista_nomes[i])
        contagem_nomes.append(contador_nomes)
    if contador_datas > 1:
        datas.append(lista_nascimento[i])
        contagem_datas.append(contador_datas)
    if contador_formacao > 1:
        formacao.append(lista_formacao[i])
        contagem_formacao.append(contador_formacao)

print('Terminei!')

escrever_arquivo_csv('frequencia_nomes.csv',nomes,contagem_nomes)
escrever_arquivo_csv('frequencia_datas.csv',datas,contagem_datas)
escrever_arquivo_csv('frequencia_formacao.csv',formacao,contagem_formacao)

plotar('Distribuição de nomes','Nomes', 'Frequência',nomes,contagem_nomes)
plotar('Distribuição de ano de nascimento','Ano de nascimento', 'Frequência',datas,contagem_datas)
plotar('Distribuição de formacao','Formação', 'Frequência',formacao,contagem_datas)