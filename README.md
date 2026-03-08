# arch_tools

A Python GUI application for simplifying Arch Linux development environment setup. `arch_tools` helps you quickly get the packages and tools you need to do dev work — including detecting or installing AUR helpers, then presenting a wide selection of developer tools you can browse and choose to install.

## Features

- **AUR helper detection** — automatically detects if `paru` or `yay` is installed
- **AUR helper installation** — installs your preferred AUR helper if none is found
- **GUI package selector** — browse and select from a wide catalog of dev tools to install (coming soon)
- **Arch-native** — uses `pacman` and AUR helpers directly; no abstraction layers

## Requirements

- Arch Linux (or Arch-based distro)
- Python >= 3.14
- [uv](https://docs.astral.sh/uv/) for package management

## Installation

```bash
git clone https://github.com/yourusername/arch_tools.git
cd arch_tools
uv sync
```

## Usage

```bash
uv run python main.py
```

## Project Structure

```
arch_tools/
├── main.py                          # Entry point
├── pyproject.toml                   # Project metadata and dependencies
├── src/
│   ├── models/                      # Data models
│   ├── services/                    # Business logic
│   │   └── aur_helper_service.py    # AUR helper detection
│   ├── tests/                       # Test suite
│   │   └── test_aur_helper_service.py
│   └── ui/                          # GUI layer (not yet implemented)
└── uv.lock
```

## Development

Run tests:
```bash
uv run pytest
```

Lint and format:
```bash
uv run ruff check .
uv run ruff format .
```

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14+ | Core language |
| uv | Environment & package management |
| pytest | Testing |
| ruff | Linting & formatting |
| pylint | Static analysis |
