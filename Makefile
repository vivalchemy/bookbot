# Variables
PYTHON_CMD := python3
MAIN_FILE := main.py
LOG_FILE := log.txt
TMP_DIR := ./tmp

.PHONY: all clean debug run

all: run

run: $(MAIN_FILE)
	@$(PYTHON_CMD) $<

clean: $(TMP_DIR)
	@rm -rf $(TMP_DIR)

debug: $(MAIN_FILE)
	@mkdir -p $(TMP_DIR)
	@$(PYTHON_CMD) $< > $(TMP_DIR)/$(LOG_FILE)
	@bat $(TMP_DIR)/$(LOG_FILE)
