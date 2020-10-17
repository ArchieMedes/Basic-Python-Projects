import random
x = True

def dice_simulator():

    print("Vamos a lanzar dados")
    dado_1 = random.randint(1,6)
    print("dado_1: ", dado_1)
    dado_2 = random.randint(1,6)
    print("dado 2: ", dado_2)
    lanzamiento_total = dado_1 + dado_2
    print("lanzamiento total: ", lanzamiento_total)


while x == True:
    dice_simulator()
    indicador = input("Presiona cualquier tecla para lanzar de nuevo... o presiona '0' para terminar el programa:\n")
    if indicador == '0':
        x = False
    else:
        x = True
