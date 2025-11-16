# Contributing to Revit System Configuration 2022

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/revit_system_john_2022.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Poetry (recommended) or pip
- Node.js (for npm scripts)

### Installation

```bash
# Install dependencies with Poetry
poetry install

# Or with pip
pip install -r requirements.txt

# Install development dependencies
poetry install --with dev

# Install Playwright browsers for E2E testing
playwright install
```

## Code Standards

### Python Code Style
- Follow PEP 8 guidelines
- Use Black for code formatting: `black .`
- Use flake8 for linting: `flake8 .`
- Use mypy for type checking: `mypy .`

### Code Formatting

```bash
# Format code
npm run format
# or
poetry run black .

# Lint code
npm run lint
# or
poetry run flake8 .

# Type check
npm run type-check
# or
poetry run mypy .
```

## Testing

All contributions should include appropriate tests.

### Running Tests

```bash
# Run all tests
npm test
# or
poetry run pytest

# Run with coverage
npm run test:coverage
# or
poetry run pytest --cov=. --cov-report=html

# Run BDD tests
npm run test:bdd
# or
poetry run pytest tests/features/

# Run E2E tests
npm run test:e2e
# or
poetry run pytest tests/e2e/
```

### Writing Tests

- Unit tests: Test individual functions and components
- BDD tests: Write feature files in `tests/features/` and step definitions in `tests/step_defs/`
- E2E tests: Test complete user workflows in `tests/e2e/`

## Pull Request Process

1. **Update Documentation**: Ensure the README and other docs are updated if needed
2. **Add Tests**: Include tests for new features or bug fixes
3. **Run Tests**: Ensure all tests pass before submitting
4. **Code Quality**: Run linting and formatting tools
5. **Descriptive Commits**: Use clear, descriptive commit messages
6. **PR Description**: Provide a detailed description of your changes

### Commit Message Guidelines

Use conventional commit messages:

- `feat: Add new feature`
- `fix: Fix bug in component`
- `docs: Update documentation`
- `test: Add tests for feature`
- `refactor: Refactor code structure`
- `style: Format code`
- `chore: Update dependencies`

## Adding New Components

To add a new hardware component analysis:

1. Create a new page file: `pages/N_Component_Name.py`
2. Follow the existing page structure
3. Import required libraries: `streamlit`, `pandas`, `plotly`
4. Add comparison data and visualizations
5. Include benchmarks and recommendations
6. Add tests for the new component

## Project Structure

```
revit_system_john_2022/
├── main.py                 # Main application
├── pages/                  # Streamlit pages
├── image/                  # Assets
├── tests/                  # Test suites
│   ├── features/          # BDD features
│   ├── step_defs/         # BDD step definitions
│   └── e2e/               # E2E tests
├── pyproject.toml         # Poetry config
├── package.json           # NPM scripts
└── README.md              # Documentation
```

## Reporting Issues

When reporting issues, please include:

- Clear description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, etc.)

## Feature Requests

Feature requests are welcome! Please include:

- Clear description of the feature
- Use case and benefits
- Possible implementation approach
- Any relevant examples

## Questions?

For questions or support, contact:
- Email: [victor@budgetapp.works](mailto:victor@budgetapp.works)

## License

By contributing, you agree that your contributions will be licensed under the ISC License.

---

Thank you for contributing to Revit System Configuration 2022!
