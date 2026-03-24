"""Módulo de análisis estático de código Python.

Detecta patrones de riesgo como SQL injection y bare except.
"""
import ast
import re

archivos = ["reservas.py", "clientes.py"]

for archivo in archivos:
    print(f"\nAnalizando archivo: {archivo}")

    with open(archivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    tree = ast.parse(codigo)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            parametros = len(node.args.args)
            if parametros > 6:
                msg = (f"[MEDIA] Long Parameter List en función "
                       f"{node.name} ({parametros} parámetros)")
                print(msg)

    if re.search(r"SELECT \* FROM .* \+ ", codigo):
        msg = "[ALTA] Posible SQL Injection detectado"
        print(msg)

    if re.search(r"except:", codigo):
        print("[MEDIA] Uso de bare except detectado")
