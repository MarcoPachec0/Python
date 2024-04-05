print('Pronto para calcular o valor do aluguel')
km = float(input('Quantos kilometros foram rodados: '))
dias = int(input('Quantos dias utilizou o carro: '))

aluguel = (60 * dias) + (0.15 * km)

print(f'O aluguel que deverá ser pago será de R${aluguel:.2f}')