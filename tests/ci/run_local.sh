# Run this script locally to make sure the project will pass all tests before pushing anything!

# Lint
pylint ./src


# Format
black .

# Unit Tests
pytest .

# Coverage
pytest --cov=./ --cov-report=xml
