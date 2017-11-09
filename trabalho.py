from scipy.integrate import quad
import numpy as np

def f(x):
    vet = []
    i = 0
    soma = 0
    while(i < 30):
        fat = fatorial(i)
        vet.append(((((-x**2)/2)**i)/fat))
        i +=1
    i = 0
    while(i < 30):
        soma = soma + vet[i]
        i += 1
    return soma

def fatorial(x):
    if((x == 1) or (x == 0)):
        return 1
    else:
        return fatorial(x-1) * x


def geraTabela():
    x = 0
    j = 0
    i = 0.0
    vet = []
    matriz = []
    while (i < 4):
        while(j < 10):
            b = i + (j/100.0)
            resultIntegral = quad(f,0,b)
            aux = (1/((2*3.14159265359)**(0.5)))
            valor = resultIntegral[0] * aux
            vet.append(valor)
            j += 1
        matriz.append(vet)
        vet = []
        i += 0.1
        j = 0
    # print("%.4f" %matriz[24][9])
    np.set_printoptions(precision=4, linewidth=100)
    print(np.matrix(matriz))
    # imprimeMatriz(matriz)


def main(args):
    # i = quad(f,0,0.01)
    # t = (1/((2*3.14159265359)**(0.5)))
    # z = i[0] * t
    # print("%.4f" % z)
    geraTabela()
    # # print(0.1+(1/10.0))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
