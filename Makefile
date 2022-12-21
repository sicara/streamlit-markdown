test:
	poetry run pytest tests --cov stmd --cov-report term --cov-report=html --cov-report xml --junit-xml=tests-results.xml

black:
	poetry run black . --check

lint:
	poetry run pylint stmd tests

isort:
	poetry run isort . --check

mypy:
	poetry run mypy stmd --explicit-package-bases --namespace-packages
