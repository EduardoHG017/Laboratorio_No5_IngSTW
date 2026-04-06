"""Módulo de análisis estático de código Python.

Detecta patrones de riesgo como SQL injection y bare except.
"""
import ast
import os
import re

ARCHIVOS = ["reservas.py", "clientes.py"]


def analizar_archivo(ruta):
    """Analiza un archivo Python en busca de patrones de riesgo.

    Args:
        ruta: Ruta absoluta al archivo a analizar
    """
    nombre = os.path.basename(ruta)
    print(f"\nAnalizando archivo: {nombre}")

    with open(ruta, "r", encoding="utf-8") as archivo:
        codigo = archivo.read()

    tree = ast.parse(codigo)

    for nodo in ast.walk(tree):
        if isinstance(nodo, ast.FunctionDef):
            parametros = len(nodo.args.args)
            if parametros > 6:
                msg = (
                    f"[MEDIA] Long Parameter List en función "
                    f"{nodo.name} ({parametros} parámetros)"
                )
                print(msg)

    if re.search(r"SELECT \* FROM .* \+ ", codigo):
        print("[ALTA] Posible SQL Injection detectado")

    if re.search(r"except:", codigo):
        print("[MEDIA] Uso de bare except detectado")


def main():
    """Ejecuta el análisis estático sobre los archivos del módulo."""
    directorio = os.path.dirname(os.path.abspath(__file__))
    for nombre_archivo in ARCHIVOS:
        ruta = os.path.join(directorio, nombre_archivo)
        analizar_archivo(ruta)


if __name__ == "__main__":
    main()
