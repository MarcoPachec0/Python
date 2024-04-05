print('Cada litro de tinta pinta 2m²')

altura = float(input('Entre com a altura: '))
largura = float(input('Entre com a largura: '))

area = altura * largura
total = area / 2

print(f'Você precisará de {total:.2f} litros de tinta')