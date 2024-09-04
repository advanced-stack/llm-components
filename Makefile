.PHONY: setup

venv:
	@python3 -m venv venv
	-ln -s venv/bin .
	-ln -s venv/bin/activate .

test:
	@bin/pytest

setup: venv
	@bin/pip3 install -U pip
	@bin/pip3 install jupyter build twine
	@bin/pip3 install -e .

# Define the package name and version
PKG_NAME := llm-components

# Define the directory where the package source code is located
PKG_DIR := $(shell pwd)

# Define the directory where the built packages will be stored
BUILD_DIR := dist

# Define the directory where the package source code will be checked out
SRC_DIR := $(PKG_DIR)/src

# Define the URL of the Git repository
GIT_REPO_URL := https://github.com/advanced-stack/$(PKG_NAME).git

# Define the command to run Python
PYTHON := python3

PKG_VERSION := 1.3.1

# Define the command to run pip
PIP := pip3

# Define the command to run setuptools
SETUPTOOLS := $(PIP) install --upgrade setuptools

# Define the command to run twine
TWINE := twine

# Define the command to run git
GIT := git

# Define the command to run the build script
BUILD := $(PYTHON) -m build

# Define the command to check the built packages
CHECK := $(TWINE) check $(BUILD_DIR)/*

# Define the command to upload the built packages
UPLOAD := $(TWINE) upload $(BUILD_DIR)/*

# Define the target to create a new Git tag
tag:
	@echo "Creating new Git tag $(PKG_VERSION)"
	@$(GIT) tag -a $(PKG_VERSION) -m "Release version $(PKG_VERSION)"

# Define the target to push the Git tag to the remote repository
push: tag
	@echo "Pushing Git tag $(PKG_VERSION) to remote repository"
	@$(GIT) push --follow-tags

# Define the target to build the package
build:
	@echo "Building package $(PKG_NAME)-$(PKG_VERSION)"
	@$(SETUPTOOLS)
	@$(BUILD)

# Define the target to check the built packages
check: build
	@echo "Checking built packages"
	@$(CHECK)

# Define the target to upload the built packages to PyPI
upload: check
	@echo "Uploading built packages to PyPI"
	@$(UPLOAD)

display-version:
	echo ${PKG_VERSION}
