nota = input('Digite as notas do aluno para saber a média: ').split(' ')

media = (int(nota[0]) + int(nota[1])) / 2
print(f'Sua média foi: {media}')
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")