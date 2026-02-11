# Backgammon en Python 

Alumno: Joaquin Basile

---
## Entorno desarrollo 🛠️

### Requisitos:
- Python 3.13
- Librerias en requirements.txt
- Make
*Se puede instalar manualmente todo (no recomendado) o usar nix-shell*

### Nix dev-shell 󱄅
#### Instalar nix
- **Linux**:
  ```sh
  $ sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install) --daemon
  ```
- **MacOS**:
  ```sh
  $ sh <(curl --proto '=https' --tlsv1.2 -L https://nixos.org/nix/install)
  ```

- **Windos**:
  ```
  mejor no uses windows 🙂
  ```
Ante cualquier duda ver la documentacion oficial en [Nixos](https://nixos.org/download/#nix-install-macos "Instalar nix")

#### Habilitar flakes
En el archivo ***~/.config/nix/nix.conf*** agregar la siguiente linea(crear si no existe)
```
experimental-features = nix-command flakes
```

#### Correr la nix-shell
  En la raiz del proyecto escribir el siguiente comando:
  ```sh 
  nix develop
  ```
Listo deberias tener la version de python, sus librerias y herramientas extras usadas en el proyecto

### Ejecutar los tests 🧪
``` sh
make test
```

---

## Reglas del juego (Simplificadas):
Generales:
- Hay dos jugadores
- Se juega por turnos alternados
- Se usan dos dados

Tablero
- El tablero consta de 4 cuadrantes
- El tablero consta de agujas donde se colocan las fichas, 24 en total

Juego
- Se empieza tirando un dado cada jugador para decidir quien juega primero
- En cada turno se tiran ambos dados
- Si sale un numero doble el jugador tiene otro turno luego de mover las fichas
- En cada turno se debera realizar el maximo numero de movimientos posibles
- Las fichas se desplazan en sentidos contrarios entre ambos jugadores
- Las fichas se moveran la cantidad de casillas que indiquen los dados (se puede usar un dado para cada ficha)
- Las fichas se pueden mover a la casilla solo si la misma no esta ocupada por 2 o más fichas rivales
- Si la casilla a la que se desplaza la ficha tiene una rival la misma es capturada y colocada fuera del tablero
- Un jugador no puede realizar movimientos si tiene fichas capturadas
- Para recuperar una ficha se tiene que hacer un movimiento valido tomando como primer casilla posible la más alejada de la meta 

Ganar
- Para ganar la partida un jugador tiene que sacar todas sus fichas del tablero
- Para poder sacar una ficha primero todas las fichas del jugador deben estar en el cuadrante más cercano a la meta
- Para poder sacar una ficha el numero del dado debe ser los movimientos exactos para salir del tablero
- Solo podrá utilizarse un número más alto del preciso para sacar una pieza cuando no quede ninguna otra en ninguna de las casillas anteriores.

