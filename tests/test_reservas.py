"""Pruebas unitarias para los módulos reservas y clientes."""
from src.reservas import (
    calcular_total,
    validar_cantidad,
    validar_fecha,
    crear_reserva,
    cancelar_reserva,
)
from src.clientes import (
    validar_nombre,
    validar_email,
    crear_cliente,
    obtener_nombre_cliente,
)


# ── Pruebas: reservas.py ──────────────────────────────────────────────────────

def test_calcular_total_correcto():
    """Verifica que el total se calcule correctamente."""
    assert calcular_total(2, 150) == 300


def test_calcular_total_con_cero():
    """Verifica que el total sea 0 si la cantidad es 0."""
    assert calcular_total(0, 150) == 0


def test_calcular_total_precio_alto():
    """Verifica el cálculo con precios altos."""
    assert calcular_total(5, 1000) == 5000


def test_validar_cantidad_valida():
    """Verifica que una cantidad positiva sea válida."""
    assert validar_cantidad(1) is True


def test_validar_cantidad_invalida():
    """Verifica que cero sea cantidad inválida."""
    assert validar_cantidad(0) is False


def test_validar_cantidad_negativa():
    """Verifica que una cantidad negativa sea inválida."""
    assert validar_cantidad(-5) is False


def test_validar_fecha_valida():
    """Verifica que una fecha en formato correcto sea válida."""
    assert validar_fecha("2025-12-31") is True


def test_validar_fecha_invalida():
    """Verifica que una fecha en formato incorrecto sea inválida."""
    assert validar_fecha("31-12-2025") is False


def test_crear_reserva_valida():
    """Verifica la creación de una reserva válida."""
    reserva = crear_reserva("Juan", "2025-12-31", 3)
    assert reserva is not None
    assert reserva["total"] == 300


def test_crear_reserva_cantidad_invalida():
    """Verifica que cantidad inválida impide crear la reserva."""
    assert crear_reserva("Juan", "2025-12-31", 0) is None


def test_crear_reserva_fecha_invalida():
    """Verifica que fecha inválida impide crear la reserva."""
    assert crear_reserva("Juan", "31-12-2025", 3) is None


def test_crear_reserva_campos_completos():
    """Verifica que la reserva contenga todos los campos esperados."""
    reserva = crear_reserva("Ana", "2025-06-15", 2)
    assert reserva["cliente"] == "Ana"
    assert reserva["fecha"] == "2025-06-15"
    assert reserva["cantidad"] == 2


def test_cancelar_reserva():
    """Verifica que la cancelación devuelve True."""
    assert cancelar_reserva(1) is True


# ── Pruebas: clientes.py ──────────────────────────────────────────────────────

def test_validar_nombre_valido():
    """Verifica que un nombre correcto sea válido."""
    assert validar_nombre("Juan") is True


def test_validar_nombre_corto():
    """Verifica que un nombre de un solo carácter sea inválido."""
    assert validar_nombre("J") is False


def test_validar_nombre_vacio():
    """Verifica que un nombre vacío sea inválido."""
    assert validar_nombre("") is False


def test_validar_nombre_solo_espacios():
    """Verifica que un nombre con solo espacios sea inválido."""
    assert validar_nombre("   ") is False


def test_validar_nombre_tipo_invalido():
    """Verifica que un tipo no-string sea inválido."""
    assert validar_nombre(123) is False


def test_validar_email_valido():
    """Verifica que un email correcto sea válido."""
    assert validar_email("usuario@ejemplo.com") is True


def test_validar_email_invalido_sin_arroba():
    """Verifica que un email sin @ sea inválido."""
    assert validar_email("usuarioejemplo.com") is False


def test_validar_email_invalido_sin_dominio():
    """Verifica que un email sin dominio sea inválido."""
    assert validar_email("usuario@") is False


def test_crear_cliente_valido():
    """Verifica la creación de un cliente válido."""
    cliente = crear_cliente("María", "maria@ejemplo.com")
    assert cliente is not None
    assert cliente["nombre"] == "María"
    assert cliente["email"] == "maria@ejemplo.com"


def test_crear_cliente_nombre_invalido():
    """Verifica que nombre inválido impide crear el cliente."""
    assert crear_cliente("", "maria@ejemplo.com") is None


def test_crear_cliente_email_invalido():
    """Verifica que email inválido impide crear el cliente."""
    assert crear_cliente("María", "no-es-email") is None


def test_crear_cliente_strip_nombre():
    """Verifica que el nombre se almacena sin espacios extra."""
    cliente = crear_cliente("  Carlos  ", "carlos@ejemplo.com")
    assert cliente["nombre"] == "Carlos"


def test_obtener_nombre_cliente_valido():
    """Verifica que se obtiene el nombre de un cliente existente."""
    cliente = {"nombre": "Carlos", "email": "carlos@ejemplo.com"}
    assert obtener_nombre_cliente(cliente) == "Carlos"


def test_obtener_nombre_cliente_none():
    """Verifica que None como argumento devuelve None."""
    assert obtener_nombre_cliente(None) is None


def test_obtener_nombre_cliente_sin_clave():
    """Verifica que un dict sin clave 'nombre' devuelve None."""
    assert obtener_nombre_cliente({"email": "x@x.com"}) is None
