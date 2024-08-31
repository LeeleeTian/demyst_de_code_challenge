# The Solutions for Data Engineering Coding Challenges

## Problem 1 - Parse fixed width file

### Running Locally

To run the tests or the main script using Docker locally, follow these steps:

1. Build the Docker Image

    Navigate to the project root directory and build the Docker image:

    ```bash
    docker build -t fixed-width-parser problem_1/
    ```

2. Run Unit Tests

    Use the RUN_TESTS=true environment variable to run the tests:

    ```bash
    docker run --rm -v $(pwd)/problem_1/output:/app/output -e RUN_TESTS=true fixed-width-parser
    ```

3. Run the Main Python Script

    Run the Docker container without the RUN_TESTS environment variable:

    ```bash
    docker run --rm -v $(pwd)/problem_1/output:/app/output fixed-width-parser
    ```

    This will execute the `fixed_width_parser.py` script inside the container and output the files in the subdirectory `/problem_1/output`.

    After running the command, check the `/problem_1/output` directory in your project root. You should see the following files:
    - `output_fixed_width.txt`: contains the fixed-width formatted data as specified in spec.json.
    - `output_data.csv`: contains the parsed, comma-separated values.


## Problem 2 - Data processing

### Running Locally for smaller files

To run the tests or the main script using Docker locally for small file, follow these steps:

1. Build the Docker Image

    Navigate to the project root directory and build the Docker image:

    ```bash
    docker build -t data-processing problem_2/
    ```

2. Run Unit Tests

    Use the RUN_TESTS=true environment variable to run the tests:

    ```bash
    docker run --rm -v $(pwd)/problem_2/output:/app/output -e RUN_TESTS=true data-processing
    ```

3. Run the Main Python Script

    - To generate a small CSV file (e.g., 0.001 GB), run the following command:

        ```bash
        docker run --rm -v $(pwd)/problem_2/output:/app/output -e TASK=generate_csv -e FILE_SIZE=0.001 -e OUTPUT_FILE=/app/output/generated_data.csv data-processing
        ```

        This will generate a small CSV file `/problem_2/output/generated_data.csv`.

    - To anonymize the generated CSV file, use the following command: 

        ```bash
        docker run --rm -v $(pwd)/problem_2/output:/app/output -e TASK=anonymize_data -e INPUT_FILE=/app/output/generated_data.csv -e OUTPUT_FILE=/app/output/anonymized_data.csv data-processing
        ```

        This will generate a small CSV file `/problem_2/output/anonymized_data.csv` with anonymous name `JOHN DOE` and address `123 Main Street, City, State`.
