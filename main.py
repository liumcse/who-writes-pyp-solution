import csv
import sys
from lib.graph import Graph

csv_file_location = 'response.csv'


def extract_from_data(data_src, pos_identifier, pos_first_choice, pos_second_choice, pos_third_choice):
    """Extracts name, 1st choice, 2nd choice and 3rd choice from data source with index that locates those info.

    Arguments:
        data_src [list] -- Rows of data obtained from CSV.
        pos_identifier [int] -- Column position of identifier (a.k.a. student name).
        pos_first_choice [int] -- Column position of 1st choice.
        pos_second_choice [int] -- Column position of 2nd choice.
        pos_third_choice [int] -- Column position of 3rd choice.

    Returns:
        list -- A list of object that contains name, 1st choice, 2nd choice and 3rd choice for further processing.
    """
    result = []
    for entry in data_src:
        # An entry must have valid identifier and one valid choice to qualify
        is_valid = entry[pos_identifier] and (
            entry[pos_first_choice] or entry[pos_second_choice] or entry[pos_third_choice])
        if not is_valid:
            continue
        result.append({
            'name': entry[pos_identifier],
            'first_choice': entry[pos_first_choice].upper(),
            'second_choice': entry[pos_second_choice].upper(),
            'third_choice': entry[pos_third_choice].upper()
        })
    return result


def main(argv):
    clean_data = []
    with open(csv_file_location, newline='') as csv_file:
        reader = csv.reader(csv_file)
        idx_identifier = -1
        idx_first_choice = -1
        idx_second_choice = -1
        idx_third_choice = -1
        data_src = []
        for idx_row, row in enumerate(reader):
            if idx_row == 0:
                for idx_col, col in enumerate(row):
                    if col:
                        print(col, idx_col)
                idx_identifier = int(
                    input("Which column contains names of students?"))
                idx_first_choice = int(
                    input("Which column contains 1st choices?"))
                idx_second_choice = int(
                    input("Which column contains 2nd choices?"))
                idx_third_choice = int(
                    input("Which column contains 3rd choices?"))
                continue
            data_src.append(row)
        clean_data = extract_from_data(
            data_src, idx_identifier, idx_first_choice, idx_second_choice, idx_third_choice)

    # Process
    graph = Graph()
    for student in clean_data:
        graph.add_student(student["name"], student["first_choice"],
                          student["second_choice"], student["third_choice"])

    graph.execute()


if __name__ == "__main__":
    main(sys.argv)
