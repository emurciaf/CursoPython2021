def multiplicar(x, y):
    return x * y

print("multiplicar con función", multiplicar(5, 4))

multiplicar_lambda = lambda x, y: x * y
print("multiplicar lambda", multiplicar_lambda(5, 4))

print(f'{(lambda x: x * 5)(5)}')