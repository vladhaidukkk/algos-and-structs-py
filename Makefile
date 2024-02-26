lock:
	@pip-compile --upgrade --output-file=requirements.txt
	@pip-compile --extra dev --upgrade --output-file=requirements-dev.txt

install:
	@pip install -r requirements.txt

sync:
	@pip-sync requirements-dev.txt

test:
	@python -m pytest tests
