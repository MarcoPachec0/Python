print('O funcionario tem direito a 15% de aumento')
salario = float(input('Favor digitar o salario atual: '))

novoSalario = salario + (salario * (15/100))

print(f'O novo salário do funcionario será de R${novoSalario:.2f}')
