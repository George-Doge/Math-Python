from sympy import sympify, SympifyError, plot, symbols
# for now this can just print a graph
# GeorgeG
# TODO add save option for graphs


def manual():
    print("This is a manual for this program. If you have some questions you can read this.")
    print("Multiplication is '*' division is '/' and root is '**'.")


if __name__ == "__main__":
    x, y = symbols("x, y")
    man = input("Do you want to read a manual? press 'y'. ")
    if man == "y":
        manual()
    p = 0

    pf = int(input("Write how many graphs do you want to print: "))
    # One time settings
    x_min = int(input("Enter minimal value for 'x' axis: "))
    x_max = int(input("Enter maximum value for 'x' axis: "))
    y_min = int(input("Enter minimal value for 'y' axis: "))
    y_max = int(input("Enter maximum value for 'y' axis: "))

    # Here you enter functions
    while p < pf:
        fun = input("Please enter a function: ")
        try:
            fun = sympify(fun)
        except SympifyError:
            print("Invalid input")
        else:
            plot(fun, (x, x_min, x_max), (y, y_min, y_max), legend=True)
        p += 1
    print("Thanks for using this program")
