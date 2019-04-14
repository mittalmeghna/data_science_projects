import math


def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first*second


def divide(first, second):
    return first/second


def square(first):
    return first**2


def cube(first):
    return first**3


def root(first):
    return math.sqrt(first)


def reciprocal(first):
    return 1/first


def main():
    print("Select Operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Root")
    print("8. Reciprocal")


if __name__ == '__main__':
    main()

Choice = input("Enter choice(1 through 8):")
First = int(input("Enter first number: "))
Second = int(input("Enter second number: "))

if Choice == "1":
     print(First, "+", Second, "=", add(First, Second))

elif Choice == "2":

    First = int(input("Enter first number: "))
    Second = int(input("Enter second number: "))
    print(First, "-", Second, "=", subtract(First, Second))

elif Choice == "3":
    First = int(input("Enter first number: "))
    Second = int(input("Enter second number: "))
    print(First, "*", Second, "=", multiply(First, Second))

elif Choice == "4":
    First = int(input("Enter first number: "))
    Second = int(input("Enter second number: "))
    print(First, "/", Second, "=", divide(First, Second))

elif Choice == "5":
    First = int(input("Enter first number: "))
    print(First, "^", 2, "=", square(First))

elif Choice == "6":
    First = int(input("Enter first number: "))
    print(First, "^", 3, "=", cube(First))

elif Choice == "7":
    First = int(input("Enter first number: "))
    print(math.sqrt(First), "=", root(First))

elif Choice == "8":
    First = int(input("Enter first number: "))
    print(1/First, "=", reciprocal(First))

else:
    print("invalid input")

