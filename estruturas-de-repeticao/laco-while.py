num = eval(input("Digite um número positivo:"))
while num < 0:
    num = eval(input("Digite um número positivo:"))


l = list()
nome = input("Digite um nome:")
while nome != '':
    l.append(nome)
    nome = input("Digite um nome:")

for n in l:
    print(n)
