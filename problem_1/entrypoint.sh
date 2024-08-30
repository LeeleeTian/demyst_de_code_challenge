#!/bin/sh

# Check if the RUN_TESTS environment variable is set to "true"
if [ "$RUN_TESTS" = "true" ]; then
    echo "Running unit tests..."
    python -m unittest discover -s tests -p "test_*.py"
else
    echo "Running main Python script..."
    python fixed_width_parser.py
fi
