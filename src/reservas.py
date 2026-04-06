"""Módulo de gestión de reservas de sistema de reservas."""
import re


def calcular_total(cantidad, precio):
    """Calcula el total multiplicando cantidad por precio."""
    return cantidad * precio


def validar_cantidad(cantidad):
    """Valida que la cantidad sea mayor a cero."""
    return cantidad > 0


def validar_fecha(fecha):
    """Valida que la fecha tenga formato YYYY-MM-DD."""
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", fecha))


def crear_reserva(cliente, fecha, cantidad):
    """Crea una nueva reserva si los datos son válidos.
    
    Args:
        cliente: Nombre del cliente
        fecha: Fecha de la reserva en formato YYYY-MM-DD
        cantidad: Cantidad a reservar
        
    Returns:
        Diccionario con datos de la reserva o None si es inválida
    """
    if validar_cantidad(cantidad) and validar_fecha(fecha):
        total = calcular_total(cantidad, 100)
        return {
            "cliente": cliente,
            "fecha": fecha,
            "cantidad": cantidad,
            "total": total
        }
    return None


def cancelar_reserva(_reserva_id):
    """Simula la cancelación de una reserva.

    Args:
        _reserva_id: ID de la reserva a cancelar (no usado en simulación)

    Returns:
        True si la cancelación fue exitosa
    """
    return True
