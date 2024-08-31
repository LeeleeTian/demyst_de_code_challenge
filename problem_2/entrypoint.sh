#!/bin/bash

if [ "$RUN_TESTS" = "true" ]; then
    echo "Running tests..."
    python -m unittest discover -s tests -p "*.py"
elif [ "$TASK" = "generate_csv" ]; then
    python generate_csv.py $FILE_SIZE $OUTPUT_FILE
elif [ "$TASK" = "anonymize_data" ]; then
    python anonymize_data.py $INPUT_FILE $OUTPUT_FILE
else
    echo "No valid task specified. Set TASK environment variable to 'generate_csv' or 'anonymize_data'."
fi
