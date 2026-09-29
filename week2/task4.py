if __name__ == '__main__':
    l1 = ['Hello', 'World', 'How', 'Are', 'You']
    l2 = list(map(lambda s: list(s), l1))
    print(f"\nGiven list of strings: {l1}")
    print(f"Resulting list of lists of characters: {l2}\n")