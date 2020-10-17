import random
x = True

# La CLASE del OBJETO (dado)
class Dado:   
    #Aquí dentro van los MÉTODOS
    def __init__(self, cara1, cara2, cara3, cara4, cara5, cara6): #Método __init__ que crea al objeto
        # Creamos las partes que nos importan del DADO
        self.cara_1 = cara1 
        self.cara_2 = cara2
        self.cara_3 = cara3
        self.cara_4 = cara4
        self.cara_5 = cara5
        self.cara_6 = cara6

    def lanzar(self, numero_de_dado): # Método LANZAR que simula el lanzamiento aleatorio de UN DADO
        self.cara_arriba = random.randint(1,6) # Un número al azar entre el 1 y el 6 almacenado en un ATRIBUTO del dado
        print("El resultado de tu", numero_de_dado , "dado fue:", self.cara_arriba)
        return self.cara_arriba

dado_1 = Dado(1,2,3,4,5,6)
dado_2 = Dado(1,2,3,4,5,6)

def simulador(x):
    while x == True: # Para que el programa se siga ejecutando hasta que el usuario cambie el valor a FALSE
        resultado_1 = dado_1.lanzar("primer")
        resultado_2 = dado_2.lanzar("segundo")
        resultado_total = resultado_1 + resultado_2
        print("El resultado total de ambos dados es:", resultado_total)
        indicador = input("Presiona ENTER para lanzar de nuevo... o presiona '0' y luego ENTER para terminar el programa:\n")
        if indicador == '0':
            x = False
        else:
            x = True

simulador(x)