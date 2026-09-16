if __name__ == '__main__': 
    zahl : int = 10
    kommazahl : float = 10.5
    text : str = "Hello, World!"
    wahrheitswert : bool = True

    output = \
        f"\nVariable of type {type(zahl).__name__} has a value: {zahl}\n" + \
        f"Variable of type {type(kommazahl).__name__} has a value: {kommazahl}\n" + \
        f"Variable of type {type(text).__name__} has a value: {text}\n" + \
        f"Variable of type {type(wahrheitswert).__name__} has a value: {wahrheitswert}\n"

    if isinstance(output, str):
        print(output)
    else:
        print("\nType error\n")