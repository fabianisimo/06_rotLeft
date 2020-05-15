import random

def entrada():
    n = random.randint(1,10)
    a =[]
    i = 0
    while i < n:
        a.append(random.randint(1,9))
        i = i+1
    d = random.randint(1,n)
    return [a,d]


datos = entrada()
print ("a: ",datos[0])
print ("largo a: ", len(datos[0]))
print ("d: ",datos[1])

def rotLeft(a,d):
    cant = 1
    while cant <= d:
        pib = a[0]
        it = 0
        while it <= len(a)-1:
            if it == len(a)-1:
                a[it] = pib
            else:
                a[it] = a[it+1]
            it = it + 1
        cant = cant + 1
    return a

print (rotLeft(datos[0],datos[1]))
