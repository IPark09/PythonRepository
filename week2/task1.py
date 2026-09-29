if __name__ == '__main__':
    sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    result = sorted(sample, key=lambda val: val[-1])
    print("\nSorting in increasing order by the last element in each tuple.")
    print(f"List before: {sample}\nList after: {result}\n")