test:
	python -m unittest discover
develop:
	nix develop ./.nix-develop-cache
cache:
	nix develop --profile .nix‑develop-cache --command true
