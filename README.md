# Laboratorio No5 IngSTW

Proyecto de reservas con CI/CD implementado.

## Estructura

- `src/`: Código fuente
- `tests/`: Pruebas unitarias
- `.github/workflows/ci.yml`: Pipeline de CI/CD
- `sonar-project.properties`: Configuración de SonarQube

## Ejecutar localmente

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m pytest
pylint src
```