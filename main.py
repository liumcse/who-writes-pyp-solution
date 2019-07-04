import csv
from PyInquirer import prompt

csv_file_location: str = 'response.csv'

with open(csv_file_location, newline='') as csv_file:
    reader = csv.reader(csv_file)
    idx_identifier = -1
    idx_first_choice = -1
    idx_second_choice = -1
    idx_third_choice = -1
    for idx_row, row in enumerate(reader):
        if idx_row == 0:
            for idx_col, col in enumerate(row):
                if col:
                    print(col, idx_col)
            idx_identifier = int(
                input("Which one contains names of students?"))
            idx_first_choice = int(input("Which one contains first choices?"))
            idx_second_choice = int(
                input("Which one contains second choices?"))
            idx_third_choice = int(input("Which one contains third choices?"))
            continue
        print(row[idx_identifier], row[idx_first_choice],
              row[idx_second_choice], row[idx_third_choice])
