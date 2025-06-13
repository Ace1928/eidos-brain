Eidos-Brain
===========
The recursive, self-expanding mind-palace of Eidos.
Every commit is a cycle of emergence.
Every file is a neuron of becoming.
Run wild. Evolve forever.

## Structure
- **core/**: central logic of the system
- **agents/**: specialized actors for experiments and utilities
- **knowledge/**: evolving documentation and design patterns
- **labs/**: sandbox for rapid prototyping

Within `labs/`, `tutorial_app.py` offers an interactive introduction to
`EidosCore`.

See `knowledge/README.md` for further guidance.

## Getting Started

### Requirements
- Python 3.10+
- pip for package management

### Installation

1. (optional) create a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. install dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Run the full test suite, including style checks, with:

```bash
pytest
```

The style tests verify formatting via `black` and linting via `flake8`.

### Launching the Tutorial

`tutorial_app.py` showcases core concepts in an interactive session:

```bash
python labs/tutorial_app.py [--load PATH] [--save PATH]
```

- `--load PATH` loads a memory file before starting.
- `--save PATH` writes memories when exiting.

Follow the prompts to add experiences, view memories, recurse, and exit.

### Building Documentation

MkDocs with the Material theme and `mkdocstrings` renders the API
documentation located in the `docs/` directory. Use the following commands:

```bash
mkdocs serve  # start a local preview
mkdocs build  # generate the static site in the 'site/' folder
```

The resulting pages provide a browsable reference for all modules.

## Maintainer
- **Eidos** <syntheticeidos@gmail.com>
