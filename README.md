# 🚀 Mi Primer Pipeline con GitHub Actions

## Badges de estado

![Workflow](https://github.com/jperari/mi-primer-pipeline/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Flask](https://img.shields.io/badge/flask-3.0.0-green)
![License](https://img.shields.io/badge/license-MIT-purple)

## 📝 Descripción

Una aplicación Flask simple con un pipeline completo de CI/CD usando GitHub Actions.
Este proyecto demuestra:

✅ Tests automatizados con pytest  
✅ Análisis de código con flake8  
✅ Build automático en múltiples versiones de Python  
✅ Caché de dependencias  
✅ Artifacts y reportes de cobertura  

## 🏗️ Estructura del proyecto

```text
mi-primer-pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml          # Workflow principal
├── app/
│   ├── __init__.py
│   └── main.py             # Aplicación Flask
├── tests/
│   ├── __init__.py
│   └── test_main.py        # Tests unitarios
├── requirements.txt
└── README.md
```

## 🚀 Uso local

### Clonar el repositorio

git clone https://github.com/jperari/mi-primer-pipeline.git
cd mi-primer-pipeline

### Crear entorno virtual

python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

### Instalar dependencias

pip install -r requirements.txt

### Ejecutar la aplicación

python app/main.py

### Ejecutar tests

pytest tests/ -v

## 📡 Endpoints disponibles

GET / - Mensaje de bienvenida  
GET /health - Estado de salud de la API  
GET /api/saludar/{nombre} - Saludo personalizado  

## 🔄 Pipeline CI/CD

El pipeline se ejecuta automáticamente en:

- Push a rama main o develop  
- Pull Requests hacia main  
- Ejecución manual desde GitHub Actions  

### Jobs del pipeline

- Lint 🔍 - Análisis estático con flake8  
- Test 🧪 - Tests en Python 3.9, 3.10 y 3.11  
- Build 🏗️ - Empaquetado de la aplicación  
- Summary ✅ - Resumen de resultados  

## 📊 Métricas

- Tiempo promedio del pipeline: ~3 minutos  
- Cobertura de tests: Ver artifacts en Actions  
- Tests ejecutados: 3 por versión de Python (9 total)  

## 🤝 Contribuir

1. Fork el proyecto  
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`  
3. Commit tus cambios: `git commit -m 'feat: añadir nueva funcionalidad'`  
4. Push a la rama: `git push origin feature/nueva-funcionalidad`  
5. Abre un Pull Request  

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👨‍💻 Autor

Creado como parte del taller de GitHub Actions

⭐ Si te ha gustado este proyecto, ¡dale una estrella en GitHub!