#Define function,Get coloumn names from a csv file
import csv

def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    reader = csv.reader(data)
    return list(reader)[0]


f = open('data.csv')
print(get_column_names(f))