from reservas import calcular_total, validar_cantidad, validar_fecha, crear_reserva


def test_calcular_total_correcto():
    assert calcular_total(2, 150) == 300


def test_validar_cantidad_invalida():
    assert validar_cantidad(0) is False


def test_crear_reserva_valida():
    reserva = crear_reserva("Juan", "2025-12-31", 3)
    assert reserva is not None
    assert reserva["total"] == 300


def test_validar_fecha_invalida():
    assert validar_fecha("31-12-2025") is False
