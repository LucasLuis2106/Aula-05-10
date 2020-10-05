time = input('Nome do time:')
derrotas = int(input('Números de derrotas:'))
empates = int(input('Números de empates:'))
vitorias = int(input('Números de vitórias:'))
pontos = vitorias * 3 + empates
perdidos = derrotas * 3 + empates * 2
print('pontos ganhos:', pontos)
print('pontos perdidos:', perdidos)