altura = input("Digite sua altura:")
sexo = input("Digite seu sexo, h para homens e m para mulheres:")

altura = eval(altura)

if sexo == "m":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print("O peso ideal é:", peso)
