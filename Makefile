PYTHON?=python3
FLAKE8=flake8

all: help

.PHONY: help clean swagger_json


help:
	@echo "help - show this help"
	@echo "clean - remove artifacts"
	@echo "doc - genegate api specification"

clean:
	@find . -name '*.py[cod]' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -rf {} +
	@find . -name '*$py.class' -exec rm -rf {} +

swagger_json:
	rm -f swagger.json
	$(PYTHON) manage.py generate_swagger swagger.json
