




print('\nOlá, sejá muito bem vindo(a)\nHoje iremos calcular o seu IMC, favor preencher o formulário:')

nome = input('\nDigite o seu nome: ').strip()
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = (peso/altura**2)


print(f'\n{nome} o seu IMC é {imc:.1f}')

print()

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc <24.9:
    print('Você está no seu peso normal')
elif imc <29.9:
    print('Você está com sobrepeso')
elif imc <34.9:
    print('Você está no índice de obesidade grau 1')
elif imc <39.9:
    print('Você está no índice de obesidade grau 2')
else:
    print('Você está no índice de obesidade grau 3 (obesidade mórbida)')

print()
print(type(nome))
print(type(idade))
print(type(peso))
print(type(altura))