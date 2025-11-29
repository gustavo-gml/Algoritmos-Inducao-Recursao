def somatorio(n):

    total = 0

    for i in range(n+1): # n + 1 serve para incluir o último termo
        total += i

    print(total)

somatorio(10)