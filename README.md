# Backgammon en Python 

Alumno: Joaquin Basile

---
## Entorno desarrollo 🛠️

### Para correr el codigo se puede:

- Descargar la version de python manualmente
y luego instalar las librerias especificadas en ***requirements.txt***

- Usar nix para levantar una dev-shell(recomendado)

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
Listo deberias tener la version de python y sus correspondientes librerias disponibles en tu terminal
