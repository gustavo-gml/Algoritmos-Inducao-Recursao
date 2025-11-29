def bonacci(n):
    if n == 1 or n == 2: #caso base
        return 1
    else:
        return bonacci(n-1) + bonacci(n-2) #caso recursivo

