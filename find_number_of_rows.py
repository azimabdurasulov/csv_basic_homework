import csv

def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    reader = csv.reader(data)
    return len(list(reader)[1:])


f = open('data.csv')
print(find_number_of_rows(f))