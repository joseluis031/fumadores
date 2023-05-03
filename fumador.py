#codigo fumadores
# -*- coding: utf-8 -*-
import threading
import time
import random
import sys
import os
import signal

#variables globales
#semaforos
mutex = threading.Semaphore(1)
sem_fumador = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0)]
#semaforos para los ingredientes
sem_ingrediente = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0)]
#semaforos para los agentes
sem_agente = [threading.Semaphore(0), threading.Semaphore(0), threading.Semaphore(0)]
#semaforo para el agente
sem_agente = threading.Semaphore(0)
#semaforo para el fumador
sem_fumador = threading.Semaphore(0)

#funcion para el agente
def agente():
    

    while True:
    
    
        sem_agente.acquire()
        print("\nEl agente esta poniendo los ingredientes")
        time.sleep(1)
        sem_ingrediente[random.randint(0,2)].release()
        sem_ingrediente[random.randint(0,2)].release()
        sem_ingrediente[random.randint(0,2)].release()
        print("\nEl agente ha puesto los ingredientes")
        time.sleep(1)
        sem_fumador.release()
    

#funcion para el fumador
def fumador(id):
    
    
    
    while True:
        sem_ingrediente[id].acquire()
        print("\nEl fumador ", id, " esta fumando")
        time.sleep(1)
        sem_agente.release()
        


#funcion para el main
def main():
    
    
    
    
    
    #creacion de los hilos
    hilo_agente = threading.Thread(target=agente)
    hilo_fumador = [threading.Thread(target=fumador, args=(0,)), threading.Thread(target=fumador, args=(1,)), threading.Thread(target=fumador, args=(2,))]
    
    #inicializacion de los hilos
    hilo_agente.start()
    hilo_fumador[0].start()
    hilo_fumador[1].start()
    hilo_fumador[2].start()
    
    #inicializacion del agente
    sem_agente.release()
    
    #espera a que los hilos terminen
    hilo_agente.join()
    hilo_fumador[0].join()
    hilo_fumador[1].join()
    hilo_fumador[2].join()
    

#funcion para el control de la interrupcion
def signal_handler(signal, frame):
        
        
        print('You pressed Ctrl+C!')
        sys.exit(0)



#funcion principal
if __name__ == "__main__":
        
        
        #control de la interrupcion
        signal.signal(signal.SIGINT, signal_handler)
        
        #ejecucion del main
        main()