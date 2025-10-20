test:
	python -m unittest discover
develop:
	nix develop ./.nix-develop-cache
