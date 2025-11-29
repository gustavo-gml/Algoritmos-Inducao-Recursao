def regressiva(i):

    print(i)

    if i <= 0: #na programação é comum que o caso base seja 0
        return
    else:
        regressiva(i-1) #passo indutivo

regressiva(10)