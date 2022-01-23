import time
import random
from datetime import datetime
def consumir_cpu(milliseconds: int):
    initial_time = current_milli_time()
    data = [0] * 100
    while current_milli_time() - initial_time < milliseconds:
        for index in range(len(data)):
            data[index] += random.randint(0, 100000) * random.random() / random.random()
    return sum(data)

def consumir_ram(cantidad: int, milliseconds: int):
    random.seed(datetime.now())
    array = [random.random() for i in range(cantidad)]
    time.sleep(milliseconds/1000.0) 
    random.seed(datetime.now())
    for i in range(cantidad):
        if array[i] < 0.5:
            array[i] = random.randint(0, 10)
    return sum(array)


def current_milli_time():
    return round(time.time() * 1000)