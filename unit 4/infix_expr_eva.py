def main():
    expr = input("Enter an infix expression: ")
    result = eval(expr)
    print("Result of ", expr, " is", result)

if __name__ == "__main__":
    main()