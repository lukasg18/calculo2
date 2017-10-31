
# funcao fatorial
def fatorial(x):
    if((x == 1) or (x == 0)):
        return 1
    else:
        return fatorial(x-1) * x

# funcao de distribuicao normal
def distribuicaoNormal(x):
    i = 0
    # while(i < )
    return ((1/((2*3.14)**(1/2))) * serieMclariun(x)) #  (1/(2.pi)) ^ -x²/2 

# calculando exp com serie de Mclariun
def serieMclariun(x):
    i = 0
    soma = 0
    while(i < 30):
        fat = fatorial(i)
        soma =  soma + ((((-x**2)/2)**i)/fat) # (((-x²)/2)^n)/n!
        # print(soma) 
        i +=1
    return soma


def main(args):
    # x = fatorial(4)
    x = distribuicaoNormal(0.00)
    # x = serieMclariun(0.00)
    print(x)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
