# Port Scanner

This is a simple Python-based port scanner that allows users to check whether specific ports on given targets (IP addresses) are open or closed.

## Features

- Scans multiple targets by separating them with a comma.
- Allows user input to specify the number of ports to scan.
- Displays whether each port is open or closed.

## Requirements

- Python 3.x
- `socket` module (comes pre-installed with Python)
- `termcolor` module (install using the command: `pip install termcolor`)

## Usage

1. Clone the repository or download the `portscanner.py` file.
2. Ensure you have the necessary dependencies installed by running:

    ```bash
    pip install termcolor
    ```

3. Run the script:

    ```bash
    python portscanner.py
    ```

4. When prompted, enter the target IP addresses separated by commas (if scanning multiple targets) and specify the number of ports to scan.

    Example:

    ```
    [*] Enter targets to scan (split them by ,): 192.168.1.1, 192.168.1.2
    [*] Enter how many Ports you want to scan: 1000
    ```

5. The script will output whether the specified ports are open or closed for each target.

## Example Output

