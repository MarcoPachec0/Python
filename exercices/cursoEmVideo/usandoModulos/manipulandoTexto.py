nome = input('Entre com seu nome: ')

print('Seu nome todo maiusculo é: ', nome.upper())
print('Seu nome com tudo minusculo é: ', nome.lower())

nomeSemEspaço = nome.replace(' ', '')
print('Seu nome tem ', len(nomeSemEspaço),' letras')

primeiroNome = nome.split()[0]
print(f'Seu primeiro nome é {primeiroNome} e ele tem', len(primeiroNome), 'letras')

