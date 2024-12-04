
CC = g++
CFLAGS = -std=c++20
RED    := \033[31m
GREEN  := \033[32m
YELLOW := \033[33m
BLUE   := \033[34m
RESET  := \033[0m

# The @ makes sure that the command itself isn't echoed in the terminal
help: # Print help on Makefile
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@grep '^[^.#]\+:\s\+.*#' Makefile | \
	sed "s/\(.\+\):\s*\(.*\) #\s*\(.*\)/`printf "\033[93m"`  \1`printf "\033[0m"`	\3 [\2]/" | \
	expand -35
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

  
build: clean # Usage `make build DAY=your_file.cpp` Build cpp projects 
	@$(CC) $(CFLAGS) -g -o binary $(DAY) \
		utils.cpp \
		-W -Wall -pedantic

style: #Usage `make style` Run the linter and code formatters
	ruff format *.py # formatter
	ruff check --fix *.py # linter

clean: # Remove all generated binaries
	@rm -rf binary 
