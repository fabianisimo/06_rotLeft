import random

def entrada():
    n = random.randint(1,9)
    a =[]
    i = 0
    while i < n:
        a.append(random.randint(1,9))
        i = i+1
    d = random.randint(1,2)
    return [a,d]

datos = entrada()
print ("a: ",datos[0])
print ("largo a: ", len(datos[0]))
print ("d: ",datos[1])


def rotLeft(a,d):
    pib = []
    quitador = 0
    for largo in range(len(a)):
        if largo < d:
            pib.append(a[largo])
        if largo < len(a)-d:
            a[largo] = a[largo+d]
        else:
            a[largo] = pib[quitador]
            quitador = quitador + 1
    return a


print (rotLeft(datos[0],datos[1]))
