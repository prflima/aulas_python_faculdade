primeiraNota = eval(input("Digite sua primeira nota:"))
segundaNota = eval(input("Digite sua segunda nota:"))

media = (0.4 * primeiraNota) + (0.6 * segundaNota)
mediaFinal = 5

if (media >= mediaFinal):
    print("Você está aprovado, media final foi:", media)
else:
    print("Você está reprovado, media final foi:", media)
