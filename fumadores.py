
from threading import Thread, Semaphore
import random

# Ingredients
paper = Semaphore(1)
tobacco = Semaphore(1)
matches = Semaphore(1)

# Agent Semaphore
agent_sem = Semaphore(1)

# Smoker Semaphore
smoker_sem = Semaphore(0)

# Helper function to simulate smoking
def smoker_func(resource1, resource2):
    while True:
        resource1.acquire()
        resource2.acquire()
        print("Smoker is smoking...")
        agent_sem.release()

# Create smokers
Thread(target=smoker_func, args=(paper, tobacco)).start()
Thread(target=smoker_func, args=(tobacco, matches)).start()
Thread(target=smoker_func, args=(paper, matches)).start()

# Agent thread
def agent_func():
    while True:
        agent_sem.acquire()
        resources = [paper, tobacco, matches]
        a, b = random.sample(resources, 2)
        print("Agent places", a, "and", b)
        if a == paper and b == tobacco:
            matches.release()
        elif a == tobacco and b == matches:
            paper.release()
        else:
            tobacco.release()
        smoker_sem.release()

Thread(target=agent_func).start()
