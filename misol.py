import random
x = 1
darajalar = []
for i in range(10):
    while True:
        random.seed(x)
        son = random.randrange(1, 101)
        if son == 18:
            break
        x += 1
    x += 1
    darajalar.append(x)
print(darajalar)
