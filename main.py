print('\033[36m=\033[m' * 45)
print('Calcule a sua quantidade ideal de água'.center(43))
print('\033[36m=\033[m' * 45)

peso = float(input('Digite o seu peso: '))
quantidade_de_agua = peso * 35

print('Conforme o seu peso de \033[1;32m{} kg\033[m você deve beber \033[1;32m{} ml\033[m de água por dia.'.format(peso, quantidade_de_agua))
