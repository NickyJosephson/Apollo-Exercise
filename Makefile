VENV_DIR = myenv
PYTHON = $(VENV_DIR)/bin/python
PIP = $(VENV_DIR)/bin/pip
MANAGE = $(PYTHON) manage.py
DB_FILE = db.sqlite3

setup:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Applying migrations..."
	$(MANAGE) makemigrations
	$(MANAGE) migrate
	@echo "Starting the server..."
	$(MANAGE) runserver 0.0.0.0:8000

clean-all:
	@echo "Removing virtual environment..."
	rm -rf $(VENV_DIR)
	@echo "Removing database file..."
	rm -f $(DB_FILE)
	@echo "Removing migration files..."
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
	@echo "Clean complete. Fresh install ready."