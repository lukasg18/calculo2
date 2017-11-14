from scipy.integrate import quad
import numpy as np

def f(x):
    vet = []
    i = 0
    soma = 0
    while(i < 30):
        fat = fatorial(i)
        soma = soma + ((((-x**2)/2)**i)/fat) # concatena uma unica expressao dentro da integral
        i +=1
    return soma # expressao a ser integrada pela biblioteca "scipy.integrate"

def fatorial(x):
    if(x <= 1):
        return 1
    return fatorial(x-1) * x

def geraTabela():
    x = 0
    j = 0
    i = 0.0
    vet = []
    matriz = []
    while (i < 4): # a variavel i varia de 0.0 ate 3.9 (coluna da tabela, veja o exemplo q a professora colocou no drive)
        while (j < 10): # linha da tabela varia de 1 a 9
            b = i + (j/100.0) # incrementando de 0.01 por 0.01
            resultIntegral = quad(f,0,b) # funcao q calcula a integral onde os parametros sao: (expressao a ser integrada, intervalo de integracao,intervalo de integracao)
            aux = (1/((2*3.14159265359)**(0.5))) # constante da formula de ditribuicao normal padrao(exmplo descrito no trabalho). 
            valor = resultIntegral[0] * aux # multiplicando o resultado da integral pela constante. o resultado do integral se encontra na primeira posicao do vetor, por isso eu multiplico pela posicao 0.
            vet.append(valor) #salvando o resultado em um vetor(linha a linha da tabela "0.1", "0.2", "0.3", ...)
            j += 1
        matriz.append(vet) # salvando a linha da tabela em uma matriz.
        vet = []
        i += 0.1
        j = 0
    np.set_printoptions(precision=4, linewidth=100) #configurando o modo de visualizacao da matriz, onde o "precision" e a quantidade de casas decimais apos a virgula e o "linewidth" e quantidade de termos a serem imprimidas em uma linha
    print(np.matrix(matriz)) # usando numpy para imprimir a matriz

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
