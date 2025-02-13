def say_hello():
    print("Hello World")


def say_bye():
    print("Goodbye Mars")


# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print("The weight in ounces is", ounces)


def count():
    for number in range(10):
        print("Number is now:", number)


# A simple euros to pounds conversion program
# It asks for a value in euros (for example 10)
# and converts it to pounds (8.7)
def euros_to_pounds():
    euros = float(input("Enter a value in euros: "))
    pounds = euros * 0.87
    print("The value in pounds is", pounds)


# Write your code here
def say_name():
    print("Jake")

def say_hello_2():
    print("hello")
    print("world")

def dollars_to_pounds():
    amount = float(input("How much do you want to convert? $"))
    CONVERSION_RATE = 1.35
    pounds = amount * CONVERSION_RATE
    print(f"${amount} converts to {pounds:.2f} pounds")

def sum_and_difference():
    num1 = float(input("What is your first number? >"))
    num2 = float(input("What is your second number? >"))
    
    num_sum = num1 + num2
    num_difference = num1 - num2

    print(f"Sum: {num_sum}\nDifference: {num_difference}")

def change_counter():
    amount_1p = int(input("How many 1ps do you have?")) * 0.01
    amount_2p = int(input("How many 2ps do you have?")) * 0.02
    amount_5p = int(input("How many 5ps do you have?")) * 0.05

    total_amount = amount_1p + amount_2p + amount_5p
    
    print(total_amount)

def ten_hellos():
    for _ in range(10):
        print("Hello World")

def zoom_zoom():
    num = int(input("Please enter a number >"))

    for i in range(num):
        print(f"Zoom {i+1}")

def count_to():
    num = int(input("What number should count to pls"))

    for i in range(num):
        print(i+1)

def count_from_to():
    num_from = int(input("What is your starting number pls >"))
    num_to = int(input("What number would you like to count to? >"))

    for i in range(num_from, num_to+1):
        print(i)

def weights_table():
    kg_to_ounce = 35.274
    
    print("KG\tOunces")
    for i in range(10, 201, 10):
        print(f"{i}\t{i * kg_to_ounce}")

def future_value():
    ANNUAL_INTEREST_PERCENTAGE = 0.35

    initial_amount = float(input("What is your inital amount? $"))
    years_to_invest = int(input("How many years would you invest? "))

    print("Year\tAmount")
    for i in range(years_to_invest):
        initial_amount = initial_amount + (initial_amount * ANNUAL_INTEREST_PERCENTAGE)
        print(f"{i+1}\t{initial_amount}")
