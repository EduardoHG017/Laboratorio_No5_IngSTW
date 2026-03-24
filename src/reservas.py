def calcular_total(cantidad, precio):
    return cantidad * precio


def validar_cantidad(cantidad):
    return cantidad > 0


def validar_fecha(fecha):
    import re
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", fecha))


def crear_reserva(cliente, fecha, cantidad):
    if validar_cantidad(cantidad) and validar_fecha(fecha):
        return {"cliente": cliente, "fecha": fecha, "cantidad": cantidad, "total": calcular_total(cantidad, 100)}
    return None


def cancelar_reserva(reserva_id):
    # Simula la cancelación de una reserva
    return True
