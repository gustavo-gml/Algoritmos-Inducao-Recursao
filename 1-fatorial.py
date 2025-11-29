def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

#exemplo de utilização
n = int(input())

n = fatorial(n)

print(n)