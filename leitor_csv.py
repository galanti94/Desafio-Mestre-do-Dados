import csv
# Módulo responsável por ler CSV

def leitor_de_csv(documento):
    f = open(documento,'r')
    leitor = list(csv.reader(f)) # Vira uma lista
    f.close()
    return leitor

if __name__ == '__main__':
    leitor = leitor_de_csv('usuario_nome_nascimento_formacao.csv')
    print(leitor[0])