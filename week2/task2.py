if __name__ == '__main__':
    num = 0
    sum = 0.0
    s1 = input("\nInput the string containing digits: ")
    for c in s1:
        if c.isdigit():
            num+=1
            sum+=float(c)
    avg = 0.0
    if num != 0:
        avg = sum/num
    print(f"Sum of digits inside of the string: {sum}")
    print(f"Average of digits inside of the string: {avg}\n")