# Alguns tipos em pyton não são mutáveis e dependendo do escopo em que se aplica
# a varíavel não irá sofrer alteração.

# Atribuindo o valor inteiro 3 a variável número
numero = 3

# A primeira função simplesmente atribui o valor inteiro 5 a variável x que é recebida pelo
# paramêtro da função.
def firstFunction(x):
    x = 5


# Vou chamar a função e passar a variável número com o valor inteiro 3
firstFunction(numero)

# Ao exibir o valor da variável número, nota-se que ainda permanece 3
# e não 5, em python, ao chamar a função é criado uma nova variável x e atribuído o valor inteiro 5
# mas a variável número não tem seu valor alterado, pois o objeto inteiro é imutável.
print((numero))

# O mesmo comportamento é diferente em listas
# pois listas são mutáveis

firstList = [3, 6, 9, 12]

def changeList(lst):
    lst[2] = 7

changeList(firstList)
print((firstList))