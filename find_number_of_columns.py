def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    
    sum = data.split("\n")
    data = sum[0].split(",")

    return len(data)

f = open('data.csv').read()
print(find_number_of_columns(f))