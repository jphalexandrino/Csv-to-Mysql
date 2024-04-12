import mysql.connector
import os
import csv
import time

# Register the initial time
start = time.time()
connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='usbw',
    database='test',
)
cursor = connection.cursor()

# CRUD
command = f'CREATE TABLE IF NOT EXISTS cnpjs(`id` int(11) not null AUTO_INCREMENT,`cnpj` varchar(20) not null,PRIMARY KEY (`id`) ) Engine=MyISAM'
cursor.execute(command)
connection.commit() # edit the database

# Define the path of the folder you want to traverse
folder = 'C:\\Users\\0403207\\Documents\\python-db\\folder'
# List the files in the specified folder
files_in_folder = os.listdir(folder)

# Iterate over each file in the list
value = 0
for file in files_in_folder:
    # Do whatever you want with each file
    full_path = os.path.join(folder, file)
    print(full_path)
    with open(full_path, encoding="ISO-8859-1", newline='') as csv_file:
        # Create a CSV reader object with the correct delimiter
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        # Iterate over the lines of the file
        for line in csv_reader:
            # Access the values of the desired columns
            # Column 0, 2, and 5 correspond to indices 0, 2, and 5 in the list
            column_0 = line[0]
            column_2 = line[2]
            column_5 = line[5]
            column = column_0 + column_2 + column_5
            command = f'INSERT INTO cnpjs (cnpj) VALUES ("{column}")'
            cursor.execute(command)
            connection.commit() 
            print('\r We are on line: %d out of 4,494,861'%value, end="")
            value = value + 1 # value it will stop at: 4,494,861
# Register the final time
end = time.time()
print('\n Total time for processing files: %.2f minutes.'%((end - start)/60))
print('Finished!!!')

# Calculate the total execution time
total_time = end - start

cursor.close()
connection.close()
