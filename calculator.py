def calculate(units):
    if units <= 100:
        return units * 1
    elif units <= 200:
        return (100 * 1) + (units - 100) * 2
    elif units <= 300:
        return (100 * 1) + (200 - 100) * 2 + (units - 200) * 3
    elif units > 300:
        return (100 * 1) + (200 - 100) * 2 + (300 - 200) * 3 + (units - 300) * 5


def main():
    units = int(input("Enter the units to calculate"))
    print(calculate(units))


if __name__ == '__main__':
    main()
