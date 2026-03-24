# Laboratorio No5 IngSTW

Proyecto de reservas con CI/CD automatizado en GitHub Actions e integración con SonarQube Cloud para gobernanza técnica.

## Estructura

- `src/`: Código fuente
- `tests/`: Pruebas unitarias  
- `.github/workflows/ci.yml`: Pipeline de CI/CD automatizado
- `sonar-project.properties`: Configuración de SonarQube Cloud

## Caracterís ticas

- ✅ Tests unitarios con pytest
- ✅ Análisis estático con pylint
- ✅ Cobertura de código con coverage
- ✅ SonarQube Cloud para quality gates
- ✅ Automación en GitHub Actions

## Ejecutar localmente

```bash
pip install -r requirements.txt
PYTHONPATH=src python -m pytest
pylint src
coverage run -m pytest && coverage xml
```