import random
def gen(sho):

    simbolos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    passw = "".join(random.choice(simbolos) for i in range(sho))
    print("La clave generada es:", passw)
    return passw
cosax= int(input("Longitud clave: "))
minji= gen(cosax)
