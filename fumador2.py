from collections.abc import Callable, Iterable, Mapping
import threading
import time
import random
from typing import Any


ingrediente = ["papel", "tabaco", "cerillas","filtros","green"]

#condiciones

condicion1 = threading.Condition()
condicion2 = threading.Condition()

class Fumador(threading.Thread):
    def __init__(self, ingredientes):
        super().__init__(self, ingredientes)
        self.ingredientes = ingredientes
        
    def run(self):
        while True:
            with condicion1:
                condicion1.wait()
                print("\nEl fumador ", self.ingredientes, " esta fumando")
                time.sleep(1)
                condicion2.notify()
                
                
class Agente(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            with condicion2:
                condicion2.wait()
                print("\nEl agente esta poniendo los ingredientes")
                time.sleep(1)
                condicion1.notify()
                condicion1.notify()
                condicion1.notify()
                print("\nEl agente ha puesto los ingredientes")
                time.sleep(1)

def main():
    
    fumadores = [Fumador(ingrediente[0]), Fumador(ingrediente[1]), Fumador(ingrediente[2]), Fumador(ingrediente[3]), Fumador(ingrediente[4])]
    agente = Agente()
    
    for fumador in fumadores:
        fumador.start()
    
    agente.start()

if __name__ == "__main__":
    main()