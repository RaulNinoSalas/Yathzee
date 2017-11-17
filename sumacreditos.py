creditos=["10","50","3"]
suma=0

def sumacreditos(creditos):
    suma=0
    for i in range(len(creditos)):
        suma+=int(creditos[i])
    print "Tienes "
    print suma
    print "creditos"

    
sumacreditos(creditos)
