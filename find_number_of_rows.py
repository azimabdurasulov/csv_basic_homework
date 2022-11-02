def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    data = data.split("\n")
    sum = []
    for i in data:
        odd = i.split(",")[0]
        sum += [odd]
    return len(sum)


f = open('data.csv').read()
print(find_number_of_rows(f))