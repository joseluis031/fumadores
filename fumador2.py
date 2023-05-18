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
                
                

                