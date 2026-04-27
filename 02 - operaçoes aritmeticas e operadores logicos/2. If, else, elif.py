while True:
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    break

media = (nota1 + nota2 + nota3) // 3

print(f'Sua média é: {media}')

if media >= 7:
    (print('Aprovado'))
elif 7 > media > 3:
    (print('Reprovado'))
elif media % 2 == 0:
    (print('Par'))
elif media % 2 != 0:
    (print('Impar'))
else:
    (print('não é possivel que vc seja tão burro assim'))


