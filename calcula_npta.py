from calculo import calcular_media_ponderada

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media_ponderada(nota1, nota2, nota3)

print("A média ponderada é:", media)
