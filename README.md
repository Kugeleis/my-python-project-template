# my-python-project-template

![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)
[![Ruff](https://github.com/Kugeleis/my-python-project-template/actions/workflows/ruff.yml/badge.svg)](https://github.com/Kugeleis/my-python-project-template/actions/workflows/ruff.yml)
[![MyPy](https://github.com/Kugeleis/my-python-project-template/actions/workflows/mypy.yml/badge.svg)](https://github.com/Kugeleis/my-python-project-template/actions/workflows/mypy.yml)
[![Pytest](https://github.com/Kugeleis/my-python-project-template/actions/workflows/pytest.yml/badge.svg)](https://github.com/Kugeleis/my-python-project-template/actions/workflows/pytest.yml)

A python project template with uv, bump-my-version, mypy, pytest, ruff and a taskfile.

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [go-task](https://taskfile.dev/)

### Installation

```bash
task install
```

## Development

### Running the project

```bash
task run
```

### Static Analysis (Lint, Format, Type Check)

```bash
task check
```

### Testing

```bash
task test
task test-cov
```

### Versioning

```bash
task bump-patch
task bump-minor
task bump-major
```
