def print_conversion(valorig, valconv) -> None:
    print(f"\n{valorig} ({type(valorig).__name__}) –> {valconv} ({type(valconv).__name__})")


if __name__ == '__main__': 
    val1 : int = 10
    print_conversion(val1, float(val1))

    val2 : float = 3.7
    print_conversion(val2, int(val2))

    val3 : int = 1
    print_conversion(val3, str(val3))

    val4 : str = "9"
    print_conversion(val4, int(val4))

    val5 : int = 0
    print_conversion(val5, bool(val5))

    print("")