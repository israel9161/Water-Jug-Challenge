from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

operations = []  # Lista para almacenar las operaciones


class Operacion(BaseModel):
    X: int
    Y: int
    Z: int


def validar_entero_positivo(valor):
    try:
        valor = int(valor)
        if valor <= 0:
            return False
    except ValueError:
        return False
    return True


@app.post("/api/operaciones")
def operaciones(op: Operacion):
    x = op.X
    y = op.Y
    z = op.Z

    # Validaciones

    if not validar_entero_positivo(x) or not validar_entero_positivo(y) or not validar_entero_positivo(z):
        return {"error": "Los valores de X, Y y Z deben ser números enteros positivos mayores a 0."}, 400

    if z > (x + y):
        return {"error": "El valor de Z no puede ser mayor que la suma de X y Y."}, 400

    if (z % x) > 0 and (z % y) > 0:
        return {"error": "El valor de Z no se puede medir con X o Y."}, 400

    if x == z or y == z:
        return {"error": "El valor de Z ya es igual a X o Y no es necesario proceder."}, 400

    # Operaciones y pasos
    steps = []

    if min(x, y, z) == y:
        steps.append({"X": 0, "Y": y, "step": "Fill Y"})
        x = y
        steps.append({"X": x, "Y": 0, "step": "Transfer Y to X"})
        while x < z:
            steps.append({"X": x, "Y": y, "step": "Fill Y"})
            x += y
            steps.append({"X": x, "Y": 0, "step": "Transfer Y to X"})
    elif min(x, y, z) == x:
        steps.append({"X": x, "Y": 0, "step": "Fill X"})
        y = x
        steps.append({"X": 0, "Y": y, "step": "Transfer X to Y"})
        while x < z:
            steps.append({"X": x, "Y": y, "step": "Fill X"})
            y += x
            steps.append({"X": 0, "Y": y, "step": "Transfer X to Y"})
    else:
        return {"error": "no solution"}, 400

    operations.append(steps)

    return {"steps": steps}


@app.get("/api/operaciones")
def obtener_operaciones():
    return {"operaciones": operations}
