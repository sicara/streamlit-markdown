# stmd

> Print markdown files in Streamlit without thinking about it!

## Project requirements

### Pyenv and `Python 3.10.6`

- Install [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions and virtual environments:
  ```bash
  curl -sSL https://pyenv.run | bash
  ```
  - If you are on MacOS and experiencing errors on python install with pyenv, follow this [comment](https://github.com/pyenv/pyenv/issues/1740#issuecomment-738749988)
  - Add these lines to your `~/.bashrc` or `~/.zshrc` to be able to activate `pyenv virtualenv`:
      ```bash
      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"
      eval "$(pyenv init --path)"
      ```
  - Restart your shell

- Install the right version of `Python` with `pyenv`:
  ```bash
  pyenv install 3.10.6
  ```

### Install poetry

- Install [Poetry](https://python-poetry.org) to manage your dependencies and tooling configs:
  ```bash
  curl -sSL https://install.python-poetry.org | python - --version 1.2.2
  ```

## Installation

### Create a virtual environment

Create your virtual environment and link it to your project folder:

```bash
pyenv virtualenv 3.10.6 stmd
pyenv local stmd
```
Now, every time you are in your project directory your virtualenv will be activated thanks to `pyenv`!

### Install Python dependencies through poetry

```bash
poetry install --no-root
```

### Install git hooks (running before commit and push commands)

```bash
poetry run pre-commit install
```

## Testing

To run unit tests, run `pytest` with:
```bash
pytest tests --cov stmd
```
or
```bash
make test
```

## Formatting and static analysis

### Code formatting with `black`

To check code formatting, run `black` with:
```bash
black . --check
```
or
```bash
make black
```

You can also [integrate it to your IDE](https://black.readthedocs.io/en/stable/integrations/editors.html) to reformat
your code each time you save a file.

### Static analysis with `pylint`

To run static analysis, run `pylint` with:
```bash
pylint stmd tests
```
or
```bash
make lint
```

### Order imports with `isort`

To check the imports order, run `isort` with:
```bash
isort . --check
```
or
```bash
make isort
```

### Type checking with `mypy`

To type check your code, run `mypy` with:
```bash
mypy stmd --explicit-package-bases --namespace-packages
```
or
```bash
make mypy
```
