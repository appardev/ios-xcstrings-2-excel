# Localization to Excel Converter

This project is designed to convert localization strings from a JSON file (`Localizable.xcstrings`) into an Excel file. The generated Excel file will contain the localization keys and their corresponding translations for different languages.

## Project Structure

- `main.py`: The main script that performs the conversion from JSON to Excel.
- `Localizable.xcstrings`: The JSON file containing the localization strings.
- `readme.md`: This readme file.
- `.gitignore`: Git ignore file to exclude the virtual environment directory.

## Requirements

- Python 3.x
- pandas library

## Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install pandas
    ```

## Usage

1. Place your `Localizable.xcstrings` file in the project directory.

2. Run the main script:
    ```sh
    python main.py
    ```

3. The script will generate an Excel file named `Localizable_<timestamp>.xlsx` in the project directory.

## Example

Given a `Localizable.xcstrings` file with the following content:

