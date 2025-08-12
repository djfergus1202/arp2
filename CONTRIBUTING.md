# Contributing to Academic Research Platform

Thank you for your interest in contributing to the Academic Research Platform! This document provides guidelines for contributing to this open-source project.

## 🤝 How to Contribute

### Reporting Issues

1. **Check existing issues** to avoid duplicates
2. **Use clear, descriptive titles** for bug reports
3. **Provide detailed information**:
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Error messages (if any)
   - Environment details (OS, Python version, etc.)

### Suggesting Features

1. **Check the roadmap** in README.md
2. **Open a feature request** with:
   - Clear description of the proposed feature
   - Use cases and benefits
   - Potential implementation approach
   - Any relevant examples or mockups

### Code Contributions

#### Development Environment Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/academic-research-platform.git
   cd academic-research-platform
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r github_requirements.txt
   ```

4. **Install development dependencies**
   ```bash
   pip install pytest black flake8 mypy pre-commit
   ```

5. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

#### Code Style Guidelines

- **Python Code Style**: Follow PEP 8
- **Line Length**: Maximum 88 characters (Black formatter)
- **Import Organization**: Use isort for import sorting
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Use Google-style docstrings

Example:
```python
def analyze_drug_trends(drug_name: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
    """Analyze drug trends using teratrend analysis.
    
    Args:
        drug_name: Name of the drug to analyze
        analysis_type: Type of analysis to perform
        
    Returns:
        Dictionary containing analysis results
        
    Raises:
        ValueError: If drug_name is invalid
    """
    pass
```

#### Code Organization

- **Utility Functions**: Place in appropriate `utils/` modules
- **Page Components**: Create new pages in `pages/` directory
- **Constants**: Define in module-level constants
- **Configuration**: Use environment variables for configuration

#### Testing

1. **Write tests** for new functionality
2. **Run tests** before submitting:
   ```bash
   pytest tests/
   ```
3. **Check code coverage**:
   ```bash
   pytest --cov=utils tests/
   ```

#### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines above

3. **Write/update tests** for your changes

4. **Update documentation** if needed

5. **Run quality checks**
   ```bash
   black .
   flake8 .
   mypy utils/
   pytest
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add teratrend analysis for drug classes"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Use a clear, descriptive title
   - Reference related issues
   - Provide detailed description of changes
   - Include screenshots for UI changes

#### Commit Message Convention

Use conventional commits format:

- `feat:` new features
- `fix:` bug fixes
- `docs:` documentation changes
- `style:` code style changes
- `refactor:` code refactoring
- `test:` adding or updating tests
- `chore:` maintenance tasks

Examples:
```
feat: add comprehensive literature review generator
fix: resolve import error in molecular docking module
docs: update API documentation for teratrend analyzer
```

## 🏗️ Project Architecture

### Core Components

1. **Streamlit App** (`app.py`): Main application entry point
2. **Page Modules** (`pages/`): Individual feature pages
3. **Utility Modules** (`utils/`): Core functionality and data processing
4. **Notebooks** (`notebooks/`): Jupyter notebooks for advanced analysis

### Key Design Principles

- **Modularity**: Each feature should be self-contained
- **Reusability**: Common functionality in utility modules
- **Performance**: Optimize for large datasets and free-tier deployment
- **User Experience**: Simple interface with advanced functionality
- **Extensibility**: Easy to add new analysis types and features

### Data Flow

1. **Input**: User uploads data or enters parameters
2. **Processing**: Utility modules process and analyze data
3. **Visualization**: Generate interactive plots and charts
4. **Output**: Display results and provide export options

## 🧪 Development Guidelines

### Adding New Analysis Types

1. **Create utility class** in appropriate `utils/` module
2. **Add page component** in `pages/` directory
3. **Update navigation** in main app
4. **Add tests** for new functionality
5. **Update documentation**

### Database Integration

- Use session state for temporary data
- Implement caching for expensive operations
- Consider memory usage for large datasets

### API Integration

- Use environment variables for API keys
- Implement rate limiting and error handling
- Provide fallback options when APIs are unavailable

### Performance Optimization

- Use Streamlit caching (`@st.cache_data`)
- Implement data sampling for large visualizations
- Optimize database queries and API calls

## 🐛 Testing

### Test Categories

1. **Unit Tests**: Individual function testing
2. **Integration Tests**: Component interaction testing
3. **UI Tests**: Streamlit app functionality testing
4. **Performance Tests**: Large dataset handling

### Test Structure

```
tests/
├── unit/
│   ├── test_statistical_tools.py
│   ├── test_nlp_processor.py
│   └── test_teratrend_analyzer.py
├── integration/
│   ├── test_data_flow.py
│   └── test_api_integration.py
└── ui/
    ├── test_app_pages.py
    └── test_user_workflows.py
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_statistical_tools.py

# Run with coverage
pytest --cov=utils tests/

# Run performance tests
pytest tests/performance/ -v
```

## 📚 Documentation

### Code Documentation

- **Docstrings**: All public functions and classes
- **Type Hints**: Function parameters and return values
- **Comments**: Complex logic and algorithms

### User Documentation

- **README.md**: Project overview and quick start
- **Wiki Pages**: Detailed feature documentation
- **API Reference**: Generated from docstrings

### Updating Documentation

1. Update docstrings for code changes
2. Update README.md for new features
3. Create wiki pages for complex features
4. Update example notebooks

## 🚀 Release Process

### Version Numbering

Use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

### Release Checklist

1. Update version numbers
2. Update CHANGELOG.md
3. Run full test suite
4. Update documentation
5. Create release notes
6. Tag release in Git

## 🙋‍♂️ Getting Help

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and community discussion
- **Wiki**: Detailed documentation and tutorials

## 📋 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment
- Respect different viewpoints and experiences

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or inflammatory comments
- Personal attacks
- Publishing private information without permission

### Enforcement

Project maintainers will enforce the code of conduct and may:
- Remove comments or contributions
- Temporarily or permanently ban contributors
- Report serious violations to appropriate authorities

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Project documentation for major features

Thank you for contributing to the Academic Research Platform! 🎉