.PHONY: help run install clean

# Color codes
CYAN := \033[36m
BOLD := \033[1m
RESET := \033[0m

# Default help target
help:  ## Display a list of available commands
	@echo ""
	@echo "$(BOLD)Makefile Commands:$(RESET)"
	@echo ""
	@echo "$(CYAN)help$(RESET)       - Display a list of available commands"
	@echo "$(CYAN)run$(RESET)        - Run the Streamlit app using Poetry"
	@echo "$(CYAN)install$(RESET)    - Install all project dependencies using Poetry"
	@echo "$(CYAN)lock$(RESET)       - Lock the project dependencies using Poetry"
	@echo "$(CYAN)format$(RESET)     - Format files using ruff library"
	@echo ""

run: ## Run the Streamlit app using Poetry
	poetry run streamlit run portfolio/streamlit_app/streamlit_app.py

install: ## Install all project dependencies using Poetry
	poetry install

lock: ## Lock project dependencies using Poetry
	poetry lock --no-update

format:
	poetry run ruff format .