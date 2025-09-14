# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Estructura inicial del proyecto con clases principales del núcleo
- Clases principales del juego:
  - `Backgammon`: Controlador principal del flujo del juego
  - `Board`: Manejo de lógica del tablero y fichas
  - `Player`: Representación de jugadores
  - `Dice`: Lógica de tirada de dados
  - `Point`: Representación de agujas/casillas que contienen fichas
  - `Judge`: Lógica para determinar el ganador del juego
  - `Scheduler`: Manejo de turnos
- Clases de interfaz de usuario:
  - `CLI`: Interfaz de línea de comandos (cli/cli.py)
  - `PygameUI`: Interfaz gráfica usando pygame (pygame_ui/pygame_ui.py)
- Documentación de reglas del juego en README.md
- Documentación de justificación de clases en JUSTIFICACION.md
- Diagrama de arquitectura del juego (backgammon-planing.excalidraw)
- **Infraestructura de testing y calidad de código:**
  - Workflow de CI/CD con GitHub Actions (`.github/workflows/CI.yml`)
  - Tests unitarios para las clases `Dice` y `Point` (`tests/test_dice.py`, `tests/test_point.py`)
  - Configuración de coverage con `.coveragerc`
  - Configuración de pylint con `.pylintrc`
  - Reportes automatizados de coverage y calidad de código (`REPORTS.md`)
  - Script para generación automática de reportes (`generate_reports.py`)

### Changed
- Actualizado README.md con reglas simplificadas del juego
- Mejorado JUSTIFICACION.md con explicación de las clases elegidas

### Technical Notes
- Se remplazo la clase `Checker` por la clase `Point` por motivos de eficiencia a la hora de guardar fichas 
- Se agrego las clases `Judge` y `Scheduler` para respetar los principios SOLID
- El proyecto utiliza Nix para el manejo del entorno de desarrollo
- Estructura de directorios organizada en `core/`, `cli/`, `test/`, y `pygame_ui/`
- **Coverage actual: 100% en las clases implementadas (`Dice`, `Point`, `exceptions`)**
- **Integración continua configurada para ejecutar tests y generar reportes automáticamente**
