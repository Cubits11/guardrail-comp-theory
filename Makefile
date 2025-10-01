.PHONY: pdf test cov clean

pdf:
cd theory && latexmk -pdf -quiet main.tex

test:
pytest

cov:
pytest --cov=src --cov-report=term-missing

clean:
cd theory && latexmk -C || true
find . -name "__pycache__" -type d -prune -exec rm -rf {} +
rm -rf .pytest_cache .coverage
