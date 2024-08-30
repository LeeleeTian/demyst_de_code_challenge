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


## Problem 2

### Data processing

- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

## Choices

- Any language, any platform
- One of the above problems or both, if you feel like it.