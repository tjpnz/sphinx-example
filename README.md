# sphinx-example

PyBuilder example demonstrating Sphinx plugin

## Installation

Clone the repo:

```bash
git clone https://github.com/tjpnz/sphinx-example.git
```

Create a new virtualenv and activate:

```bash
virtualenv <path>/my_virtualenv
. <path>/my_virtualenv/bin/activate
```

Install pybuilder:

```bash
pip install pybuilder
```

Inside your sphinx-example directory, run:

```bash
pyb install_dependencies publish
```

## Usage

To generate Sphinx documentation execute pyb with the sphinx_generate_documentation target:

```bash
pyb sphinx_generate_documentation
```

You can now browse the generated Sphinx html docs under docs/_build/index.html

## License

Licensed under [The MIT License (MIT)](LICENSE).
