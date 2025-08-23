# Contributing to Agent Builder

Thank you for your interest in contributing to Agent Builder! We welcome contributions from the community.

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/The-Swarm-Corporation/agents-builder.md.git
   cd agents-builder.md
   ```
3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]
   ```

## 📋 Development Guidelines

### Code Style

We use Black for code formatting and Flake8 for linting:

```bash
# Format code
black .

# Check linting
flake8 .

# Type checking
mypy agent_builder/
```

### Testing

Run tests before submitting:

```bash
# Run all tests
python tests/test_simple.py

# Run demo to verify functionality
python examples/demo.py
```

### Commit Messages

Use clear, descriptive commit messages:

```
Add: New feature description
Fix: Bug fix description  
Update: Enhancement description
Docs: Documentation changes
Test: Test-related changes
```

## 🏗️ Architecture

The codebase is organized as follows:

```
agent_builder/
├── __init__.py           # Package exports
├── sdpp_builder.py       # Core AgentBuilder class
├── simple_builder.py     # Legacy SimpleAgent (compatibility)
└── metaprompt.md         # AI assistant system prompt
```

### Key Classes

- **AgentBuilder**: Main class implementing three-tier architecture
- **AgentBuilderMode**: Enum for Basic, AI-Assisted, Expert modes
- **AgentBuilderMetrics**: Performance and quality tracking
- **ValidationResult**: Prompt quality assessment

## 📝 Types of Contributions

### 1. Bug Reports

When filing an issue, please include:

- **Environment**: OS, Python version, package versions
- **Steps to reproduce**: Minimal example
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Error messages**: Full traceback if applicable

### 2. Feature Requests

For new features:

- **Use case**: Why is this needed?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches
- **Breaking changes**: Impact on existing code

### 3. Code Contributions

#### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test your changes**
   ```bash
   python tests/test_simple.py
   python examples/demo.py
   ```

4. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: Your descriptive commit message"
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request**
   - Use a clear title and description
   - Reference related issues
   - Include screenshots if UI changes

#### Code Review Checklist

- [ ] Code follows project style guidelines
- [ ] Tests pass
- [ ] New functionality is tested
- [ ] Documentation is updated
- [ ] No breaking changes (or clearly documented)
- [ ] Performance impact considered

## 🎯 Priority Areas

We especially welcome contributions in these areas:

### High Priority
- **Bug fixes** in core functionality
- **Performance optimizations**
- **Documentation improvements**
- **Windows compatibility fixes**

### Medium Priority
- **New prompt templates** for common use cases
- **Additional AI provider integrations**
- **Enhanced validation rules**
- **UI/UX improvements**

### Future Considerations
- **Web interface** for non-technical users
- **Team collaboration features**
- **Advanced analytics dashboard**
- **Plugin system** for extensibility

## 🧪 Testing Guidelines

### Running Tests

```bash
# Core functionality
python tests/test_simple.py

# Interactive demo
python examples/demo.py

# Test all modes programmatically
python -c "
from agent_builder import AgentBuilder, AgentBuilderMode
for mode in AgentBuilderMode:
    builder = AgentBuilder(mode=mode, interactive=False)
    print(f'{mode.value}: Working ✓')
"
```

### Writing Tests

When adding new features, include tests that:

- Test the happy path
- Test edge cases
- Test error conditions
- Validate input/output formats
- Check performance expectations

Example test structure:
```python
def test_new_feature():
    # Arrange
    builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
    
    # Act  
    result = builder.new_feature()
    
    # Assert
    assert result is not None
    assert isinstance(result, ExpectedType)
```

## 📚 Documentation

### Updating Documentation

When making changes that affect users:

1. **Update README.md** for new features
2. **Update docstrings** for code changes
3. **Add examples** for new functionality
4. **Update type hints** for better IDE support

### Documentation Style

- Use clear, concise language
- Include code examples
- Provide both basic and advanced usage
- Link to related functionality

## 🔧 Development Environment

### Recommended Setup

```bash
# Install development dependencies
pip install -e .[dev]

# Pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
```

### IDE Configuration

**VS Code** (recommended settings):
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.formatting.provider": "black",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true
}
```

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help newcomers get started
- Celebrate diverse perspectives

### Communication

- **Issues**: For bugs and feature requests
- **Discussions**: For questions and ideas
- **Pull Requests**: For code contributions
- **Email**: For sensitive matters

## 🎉 Recognition

Contributors are recognized in:

- **CONTRIBUTORS.md** file
- **Release notes** for significant contributions
- **GitHub contributors** section

## ❓ Questions?

- Check existing [Issues](https://github.com/The-Swarm-Corporation/agents-builder.md/issues)
- Start a [Discussion](https://github.com/The-Swarm-Corporation/agents-builder.md/discussions)
- Review the [Documentation](docs/)

Thank you for contributing to Agent Builder! 🚀