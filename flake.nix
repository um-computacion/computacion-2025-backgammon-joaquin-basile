{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.x86_64-linux.default = pkgs.mkShell {
      packages = [
        pkgs.zsh
        (pkgs.python3.withPackages (ps: with ps; [
          pytest
          coverage
          requests
          pandas
          numpy
          matplotlib
          seaborn
          scipy
          scikit-learn
          statsmodels
          lxml
          beautifulsoup4
          pylint
        ]))
      ];

      shell = pkgs.zsh;

      shellHook = ''
        echo -e "\033[1;36m🚀 Bienvenido al entorno de desarrollo del proyecto Backgammon 🚀\033[0m"
        echo -e "\033[1;33mEjecutando tests con coverage...\033[0m"

        coverage run -m unittest discover -s tests -p "*.py"
        coverage report -m || echo -e "\033[1;31m⚠️  No se encontraron tests o coverage falló.\033[0m"
        zsh
      '';

    };
  };
}
