def factorial (value : int) -> int:
    result = 1
    for i in range(2, value+1):
        result *= i
    return result


if __name__ == '__main__': 
    while True:
        try:
            value = int(input("\nInput non-negative integer value to calculate the factorial: "))

            if value >= 0:
                print(f"\n{value}! = {factorial(value)}\n")
                break

            print ("\nThe input value should be non-negative. Try again.")

        except ValueError:
            print("\nThe input value should be an integer. Try again.")