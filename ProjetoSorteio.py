#Entrada de dados

nome = input("Digite o nome do doador: ")
valor = int(input("Digite o valor doado: "))

#Dividindo valor por 10 para calcular a quantidade de entradas no listaSorteio

qtd = valor//10
listaSorteio = []

#Incluindo a quantidade de vezes que o nome de cada doador aparecerá na lista

for i in range(0, qtd):
    listaSorteio.append(nome)

#Perguntando se usuário deseja continuar

continuar = input("Deseja incluir mais um doador? s/Sim n/Não")
while continuar != "s" and continuar != "n":
    continuar = input("Resposta incorreta, tente novamente. Deseja inserir mais dados? s/sim n/não ")

#Loop While caso usuário queira incluir mais doadores

while True:
    if continuar == "s":
        nome = input("Digite o nome do doador: ")
        valor = int(input("Digite o valor doado: "))
        qtd = valor // 10
        for i in range(0, qtd):
            listaSorteio.append(nome)
        continuar = input("Deseja incluir mais um doador? s/Sim n/Não")
    elif continuar == "n":
        break
    else:
        continuar = input("Resposta incorreta, tente novamente. Deseja inserir mais dados? s/sim n/não ")
    print(listaSorteio)

# Sorteio do ganhador

import random
random.shuffle(listaSorteio)
sorteado = random.choice(listaSorteio)
print("O ganhador é: {}".format(sorteado))