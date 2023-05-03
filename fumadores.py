import threading
import time
import random

class Agent(threading.Thread): #clase agente
    def __init__(self, sem_ingrediente, sem_agente): #constructor
        threading.Thread.__init__(self) #constructor de la clase padre
        self.sem_ingrediente = sem_ingrediente  #semaforo de los ingredientes
        self.sem_agente = sem_agente    #semaforo del agente
    def run(self):  
        while True: #ciclo infinito
            self.sem_agente.acquire()   #semaforo del agente
            print("\nEl agente esta poniendo los ingredientes") 
            time.sleep(1)   
            self.sem_ingrediente[random.randint(0,4)].release() #semaforo de los ingredientes
            self.sem_ingrediente[random.randint(0,4)].release()
            self.sem_ingrediente[random.randint(0,4)].release()
            self.sem_ingrediente[random.randint(0,4)].release()
            self.sem_ingrediente[random.randint(0,4)].release()

            print("\nEl agente ha puesto los ingredientes")
            time.sleep(1)
            self.sem_fumador.release()  #semaforo del fumador
            
class Smoker(threading.Thread): #clase fumador
    def __init__(self, id, sem_ingrediente, sem_fumador, sem_agente): #constructor
        threading.Thread.__init__(self) #constructor de la clase padre
        self.id = id    #id del fumador
        self.sem_ingrediente = sem_ingrediente  #semaforo de los ingredientes
        self.sem_fumador = sem_fumador  #semaforo del fumador
        self.sem_agente = sem_agente    #semaforo del agente
    def run(self):
        while True: #ciclo infinito
            self.sem_ingrediente[self.id].acquire() #semaforo de los ingredientes
            print("\nEl fumador ", self.id, " esta fumando")
            time.sleep(1)
            self.sem_agente.release()   #semaforo del agente
    
def main():
    sem_ingrediente = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0)] #semaforos para los ingredientes
    sem_fumador = threading.Semaphore(0) #semaforo para el fumador
    sem_agente = threading.Semaphore(0)  #semaforo para el agente
    hilo_agente = Agent(sem_ingrediente, sem_agente)   #creacion del hilo del agente
    hilo_fumador = [Smoker(0, sem_ingrediente, sem_fumador, sem_agente), Smoker(1, sem_ingrediente, sem_fumador, sem_agente), Smoker(2, sem_ingrediente, sem_fumador, sem_agente), Smoker(3, sem_ingrediente, sem_fumador, sem_agente), Smoker(4, sem_ingrediente, sem_fumador, sem_agente)] #creacion de los hilos de los fumadores
    hilo_agente.start() #inicializacion del hilo del agente
    hilo_fumador[0].start() #inicializacion del hilo del fumador
    hilo_fumador[1].start()
    hilo_fumador[2].start()
    hilo_fumador[3].start()
    hilo_fumador[4].start()
    sem_agente.release()    #semaforo del agente
    
if __name__ == "__main__":
    main()