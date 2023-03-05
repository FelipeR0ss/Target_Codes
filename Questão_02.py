def fibonacci(numero):
    x, y = 0, 1

    while y < numero:
        x, y = y, x + y
    
    if y == numero:
        return True
    
    else:
        return False

numero = int(input('Informe o número inicial: '))

if fibonacci(numero):
    print('O número informado pertence à sequência de Fibonacci.')

else:
    print('O número informado não pertence à sequencia de Fibonacci.')