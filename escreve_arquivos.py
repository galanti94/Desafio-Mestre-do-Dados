import csv

def escrever_arquivo_csv(nome_arquivo, parametro, contagem_parametro):
    arquivo = open(nome_arquivo, 'w', newline='')
    writer = csv.writer(arquivo)
    qtd_nomes = len(parametro)
    for x in range(0, qtd_nomes):
        writer.writerow((parametro[x], contagem_parametro[x]))
    arquivo.close()
