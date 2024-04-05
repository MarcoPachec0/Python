import math
co = float(input('Favor entrar com o cateto oposto: '))
ca = float(input('Favor entrar com o cateto adjacente: '))

hipotenusa = math.hypot(co, ca)

print(f'A hipotenusa nesse caso será de {hipotenusa:.2f}')