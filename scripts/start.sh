#!/bin/bash

# Function to activate the virtual environment
activate_venv() {
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        .venv\Scripts\activate  # For Windows
    else
        source .venv/bin/activate  # For Unix-based systems (Linux, macOS)
    fi
}

# Check if the virtual environment is already activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment is not activated. Activating now..."
    if [ -d ".venv" ]; then
        activate_venv
    else
        echo "Virtual environment not found. Creating and activating..."
        python3 -m venv .venv
        activate_venv
    fi
else
    echo "Virtual environment is already activated."
fi

# Upgrade pip
python -m pip install --upgrade pip

# Install packages from requirements.txt if it exists
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found"
    exit 1
fi
