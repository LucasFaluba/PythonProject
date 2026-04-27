idade = int(input("Digite sua idade: "))

if idade >= 18:
    maioridade = 'Maior de idade'
else:
    maioridade = 'Menor de idade'

cnh = input("Você possui CNH?(s/n): ")

if cnh == 's':
    cnh = 'Possui'
else:
    cnh = 'Não Possui'

if maioridade == 'Menor de idade' and cnh == 'Possui':
    print('Mentiroso, criminoso')

elif maioridade == 'Maior de idade' and cnh == 'Possui':
    print('Você pode dirigir')

elif maioridade ==  'Maior de idade' and cnh == 'Não Possui':
    print('Você não pode dirigir')

elif maioridade == 'Menor de idade':
    print('Você não pode dirigir')