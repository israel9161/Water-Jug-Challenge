import sys

def validar_entero_positivo(valor):
    try:
        valor = int(valor)
        if valor <= 0:
            return False
    except ValueError:
        return False
    return True


x = 1
y = 12
z = 10

# Validaciones

if not validar_entero_positivo(x) or not validar_entero_positivo(y) or not validar_entero_positivo(z):
    print({"error": "Los valores de X, Y y Z deben ser números enteros positivos mayores a 0."})
    sys.exit()

if z > (x + y):
    print({"error": "El valor de Z no puede ser mayor que la suma de X y Y."})
    sys.exit()

if (z % x) > 0 and (z % y) > 0:
    print({"error": "El valor de Z no se puede medir con X o Y."})
    sys.exit()

if x == z or y == z:
    print({"error": "El valor de Z ya es igual a X o Y no es necesario proceder."})
    sys.exit()

# Operaciones y pasos


if min(x, y, z) == y:
    print({"X": 0, "Y": y, "step": "Fill Y"})
    x = y
    print({"X": x, "Y": 0, "step": "Transfer Y to X"})
    while x < z:
        print({"X": x, "Y": y, "step": "Fill Y"})
        x += y
        print({"X": x, "Y": 0, "step": "Transfer Y to X"})
elif min(x, y, z) == x:
    print({"X": x, "Y": 0, "step": "Fill X"})
    y = x
    print({"X": 0, "Y": y, "step": "Transfer X to Y"})
    while y < z:
        print({"X": x, "Y": y, "step": "Fill X"})
        y += x
        print({"X": 0, "Y": y, "step": "Transfer X to Y"})
else:
    print({"error": "no tiene solucion"})



