import matplotlib.pyplot as plt
import numpy

def plotar(titulo, nome1, nome2, listax, listay):
    plt.bar(listax, listay, color='red')
    plt.xlabel(nome1)
    plt.ylabel(nome2)
    plt.title(titulo)
    plt.show()

if __name__ == '__main__':
    lista1 = [1,2,3,4,5,6]
    lista2 = [1,2,3,4,5,6]
    plotar('Lista 1 versus lista 2','lista1', 'lista2', lista1, lista2)