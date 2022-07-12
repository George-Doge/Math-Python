from sympy import sympify, SympifyError, plot, Symbol
# for now this can just print a graph
# George-Doge


def manual():
    print("This is a manual for this program. If you have some questions you can read this."
          "Multiplication is '*' division is '/' and root is '**'.\nProgram can only work with one variable 'x'."
          "You can save your graphs, all you need to do is to choose a name.\nProgram saves them in .png "
          "format and into folder where this Python file is.\n")


def printing():
    fun = input("Please enter a function: ")
    try:
        fun = sympify(fun)
    except SympifyError:
        print("Invalid input. Check manual for help")
    else:
        picture = plot(fun, (x, x_min, x_max), legend=True)
    saving(picture)


def saving(picture):
    an = input("Do you want to save your picture? Press 'y' ")
    if an == "y":
        name = input("Choose a name for your picture ")
        picture.save(f"{name}.png")


if __name__ == "__main__":
    x = Symbol("x")
    man = input("Do you want to read a manual? press 'y'. ")
    if man == "y":
        manual()
    p = 0

    pf = int(input("Write how many graphs do you want to print: "))
    # Settings, which apply to all printed graphs
    x_min = int(input("Enter minimal value for 'x' axis: "))
    x_max = int(input("Enter maximum value for 'x' axis: "))

    # Here you enter functions Python will print
    while p < pf:
        printing()
        p += 1
    print("Thanks for using this program")
