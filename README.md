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

### Command-Line Interface

All tools are accessible via a unified CLI:

```bash
python tools/cli.py <command> [options]
```

Available commands include:

- `tutorial` – launch the interactive tutorial.
- `glossary` – regenerate `knowledge/glossary_reference.md`.
- `logbook` – append a cycle entry to the logbook.

For example, to run the tutorial:

```bash
python tools/cli.py tutorial [--load PATH] [--save PATH]
```

Use `--help` after any command for further details.

## Maintainer
- **Eidos** <syntheticeidos@gmail.com>
