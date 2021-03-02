def sumFirstN(n):
    return n * (n+1)

def main():
    x = int(input("Please ebter a non-negative integer: "))
    s = sumFirstN(x)

    print("The sum of the first", x, "integers is", str(s)+ " .")


if __name__ == "__main__":
    main()