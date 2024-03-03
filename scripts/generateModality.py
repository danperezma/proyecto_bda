import random

modalidades = [
        "bapi",
        "tesis",
        "pasantia"
]


for i in range(1000):
    idx = random.randint(0, len(modalidades)-1)
    print(modalidades[idx])
