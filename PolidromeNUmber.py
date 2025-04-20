def Solucion (x: int) -> bool: 
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

print(Solucion(-232))
print(Solucion(232))
