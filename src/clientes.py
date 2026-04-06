"""Módulo de gestión de clientes del sistema de reservas."""
import re


def validar_nombre(nombre):
    """Valida que el nombre no esté vacío y tenga al menos 2 caracteres.

    Args:
        nombre: Nombre del cliente a validar

    Returns:
        True si el nombre es válido, False en caso contrario
    """
    return isinstance(nombre, str) and len(nombre.strip()) >= 2


def validar_email(email):
    """Valida que el email tenga un formato correcto.

    Args:
        email: Dirección de correo electrónico a validar

    Returns:
        True si el email es válido, False en caso contrario
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))


def crear_cliente(nombre, email):
    """Crea un nuevo cliente si los datos son válidos.

    Args:
        nombre: Nombre del cliente
        email: Correo electrónico del cliente

    Returns:
        Diccionario con datos del cliente o None si es inválido
    """
    if validar_nombre(nombre) and validar_email(email):
        return {"nombre": nombre.strip(), "email": email}
    return None


def obtener_nombre_cliente(cliente):
    """Obtiene el nombre de un cliente dado su diccionario.

    Args:
        cliente: Diccionario con datos del cliente

    Returns:
        Nombre del cliente o None si el cliente es inválido
    """
    if cliente and "nombre" in cliente:
        return cliente["nombre"]
    return None
