print('Você tem direto a 5% de desconto')
valor = float(input('favor entrar com o valor da compra: '))

preçoFinal = valor - (valor * (5/100))

print(f'Seu valor com 5% de desconto será de R${preçoFinal:.2f}')
