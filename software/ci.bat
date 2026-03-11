@echo off
echo ==============================
echo INICIANDO PIPELINE LOCAL DE CI
echo ==============================

echo.
echo [1/2] Ejecutando pruebas unitarias...
python -m pytest -v software\test_reservas.py
if errorlevel 1 (
    echo.
    echo ERROR: Fallaron las pruebas unitarias.
    exit /b 1
)

echo.
echo [2/2] Ejecutando analisis estatico...
python -m pylint --exit-zero software\reservas.py software\clientes.py
if errorlevel 1 (
    echo.
    echo ERROR: Fallo el analisis estatico.
    exit /b 1
)

echo.
echo PIPELINE EJECUTADO CON EXITO.
pause
