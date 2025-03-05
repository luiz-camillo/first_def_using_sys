
import sys


def standard_strings(text):
    return text.title()

nome = input('Qual o seu nome? :').strip()

nome1 = standard_strings(nome)

idade = int(input('Qual a sua idade? (Valor entre 1 e 100, se tiver mais de 100 feche o programa imediatamente):'))

if idade > 100:
    print("Idade inválida! O programa será fechado.")
    sys.exit()  # Fecha o programa imediatamente

while idade <1 or idade >100:
    idade = int(input('Entrada inválida, tente novamente: '))

print(f'\nO seu nome é {nome1} e você tem {idade} anos de idade\n')
