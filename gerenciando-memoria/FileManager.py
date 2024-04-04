# Abrindo o arquivo teste na pasta arquivos e escrevendo Hello World

def writeFile(fileName, text):
    with open(fileName, "w") as f:
        for line in text:
            f.write(f'{line}\n')
        f.close()

writeFile("arquivos/teste.txt", ['Hello', 'World'])

# Acessando o arquivo de texto contido na pasta arquivos chamado teste
# e exibir seu conteúdo no console
with open("arquivos/teste.txt", "r") as f:
    data = f.read()
    print(data)
    f.close()

# Agora vou adicionar outro texto, sem sobrescrever o anterior hello world
def addTextEndLine(fileName, text):
    with open(fileName, "a") as f:
        f.write(text)
        f.close()

addTextEndLine("arquivos/teste.txt", 'Meu nome é Paulo Ricardo')

with open("arquivos/teste.txt", "r") as f:
    data = f.read()
    print(data)
    f.close()

# output
# Hello
# World
# Meu nome é Paulo Ricardo
