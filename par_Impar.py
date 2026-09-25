n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))
n3 = float (input("Digite o terceiro número: "))
media = (n1 + n2 + n3) / 3
print(f" A média:  {media:.2f}")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")