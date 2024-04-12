# CSV to MySQL

## Description
The CSV to MySQL script automates the process of transferring data from CSV files into a MySQL database table. It reads CSV files from a specified folder, extracts desired columns, and inserts the data into the MySQL table. Progress and total processing time are displayed during execution.

## Setup
Before running the script, ensure you have the necessary dependencies installed:
- `mysql-connector-python`: `pip install mysql-connector-python`

## Configuration
Adjust the following variables in the script to match your MySQL setup:
- `host`, `port`, `user`, `password`, `database`: MySQL connection details
- `folder`: Path to the folder containing your CSV files

## Usage
1. Clone this repository.
2. Navigate to the project directory.
3. Modify the script `csv_to_mysql.py` with your MySQL connection details and folder path.
4. Run the script: `python csv_to_mysql.py`

## Contributing
Contributions are welcome! Feel free to submit pull requests or report issues.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- GitHub: sondercs

For any questions or suggestions, feel free to reach out!
