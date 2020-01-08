from leitor_csv import leitor_de_csv
# Módulo responsável por separar informações do CSV

def somente_nome(arquivo):
    somente_nome = []
    arquivo_completo = leitor_de_csv(arquivo)
    tamanho_do_arquivo = len(arquivo_completo)
    for indice in range(2, tamanho_do_arquivo):
        somente_nome.append(arquivo_completo[indice][0])
    return somente_nome

def somente_nascimento(arquivo):
    somente_ano_de_nascimento = []
    arquivo_completo = leitor_de_csv(arquivo)
    tamanho_do_arquivo = len(arquivo_completo)
    for indice in range(2, tamanho_do_arquivo):
        somente_ano_de_nascimento.append(arquivo_completo[indice][1])
    return somente_ano_de_nascimento

def somente_formacao(arquivo):
    somente_formacao = []
    arquivo_completo = leitor_de_csv(arquivo)
    tamanho_do_arquivo = len(arquivo_completo)
    for indice in range(2, tamanho_do_arquivo):
        somente_formacao.append(arquivo_completo[indice][2])
    return somente_formacao

if __name__ == '__main__':
    nome = somente_nome('usuario_nome_nascimento_formacao.csv')
    nome.sort()
    for i in range(50): print(nome[i])
