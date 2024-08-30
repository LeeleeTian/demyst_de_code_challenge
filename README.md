# The Solutions for Data Engineering Coding Challenges

## Problem 1 - Parse fixed width file

### Run Using Docker

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd problem_1
    ```

2. Build the Docker image:

    ```bash
    docker build -t fixed-width-parser .
    ```

3. Run the Docker container:

    ```bash
    docker run --rm -v $(pwd):/app fixed-width-parser
    ```

   This will execute the `fixed_width_parser.py` script inside the container and output the files in your project directory.

    After running the Docker container, check the current directory on your host machine for the files output_fixed_width.txt and output_data.csv.
    Open and verify these files to ensure that:
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