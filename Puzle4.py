def puzle4(x, y, z):
    NX = not x
    NY = not y
    NZ = not z

    return NX, NY, NZ

valores = [(False, False, False), (False, False, True), (False, True, False),
          (False, True, True), (True, False, False), (True, False, True),
          (True, True, False), (True, True, True)]

for x, y, z in valores:
    resultado = puzle4(x, y, z)
    print(f"X: {x}, Y: {y}, Z: {z} => NOT(X): {resultado[0]}, NOT(Y): {resultado[1]}, NOT(Z): {resultado[2]}")
