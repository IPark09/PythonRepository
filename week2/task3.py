if __name__ == '__main__':
    sample = [{'make': ' Google ', 'model': 216, 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    result = sorted(sample, key=lambda val: float(val['model']), reverse=True)
    print("\nSorting in decreasing order by the model number in each dictionary.\n")
    print(f"List before: {sample}\n\nList after: {result}\n")