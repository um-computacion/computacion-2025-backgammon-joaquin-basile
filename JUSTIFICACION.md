# Justificaciones de backgammon

### ¿Por que uso nix?
Nix es, entre muchas otras cosas, un gestor de paquetes el cual permite crear shells para desarrollo
de forma que cualquiera que tenga Nix instalado pueda iniciar una shell con todos los programas y librerías necesarios
para correr el mismo. Además, mi SO es NixOS, por lo que la forma tradicional de instalar librerías
causa conflictos por cómo funciona el mismo [video de referencia](https://www.youtube.com/watch?v=6fftiTJ2vuQ).

### Clases elegidas
Se elgieron como clases:
- Backgammon
- Board
- Scheduler
- Player
- Dice
- Point
- Judge
- CLI
- PyGameUI

Se agregaron dos clases aparte de las indicadas por el documento para respetar los principios SOLID (Judge, Scheduler) y se cambio la clase **Checker** por **Point** que representa a una aguja que puede contener fichas
