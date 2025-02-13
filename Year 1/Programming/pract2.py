import math

def square_root_calculator():
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        print("Square root is undefined for negative numbers.")
    else:
        sqrt_value = math.sqrt(num)
        print("Square root:", round(sqrt_value, 2))

def sine_and_cosine():
    angle = float(input("Enter an angle in degrees: "))
    angle_in_radians = math.radians(angle)  # converts degrees to radians
    sine_value = math.sin(angle_in_radians)
    cosine_value = math.cos(angle_in_radians)
    print("Sine of the angle:", round(sine_value, 2))
    print("Cosine of the angle:", round(cosine_value, 2))

# Add your solutions to the programming exercises here.
# Remember that the `math` module is already imported for you (do not import it again!)
def speed_calculator():
    distance_traveled = float(input("How far did you travel? (km) "))
    distance_duration = float(input("How long did you travel for?"))

    speed = distance_traveled / distance_duration

    print(speed)

def circumference_of_circle():
    circle_radius = float(input("What is the radius of your circle? >"))
    circle_circumference = 2 * math.pi * circle_radius

    print(circle_circumference)

def area_of_circle():
    circle_radius = float(input("What is the radius of your circle? >"))
    circle_area = math.pi * circle_radius**2

    print(circle_area)

def cost_of_pizza():
    COST_PER_CM = 3.5
    
    pizza_diameter = float(input("What is the diameter of the pizza? (cm) "))
    pizza_area = math.pi * (pizza_diameter / 2)**2
    pizza_cost = pizza_area * COST_PER_CM

    print(pizza_cost)
    
def slope_of_line():
    x_1 = float(input("What is your first x co-ordinate? "))
    y_1 = float(input("What is your first y co-ordinate? "))
    x_2 = float(input("What is your second x co-ordinate? "))
    y_2 = float(input("What is your second y co-ordinate? "))

    slope = (y_2 - y_1) / (x_2 - x_1)

    print(slope)

def distance_bewteen_points():
    x_1 = float(input("What is your first x co-ordinate? "))
    y_1 = float(input("What is your first y co-ordinate? "))
    x_2 = float(input("What is your second x co-ordinate? "))
    y_2 = float(input("What is your second y co-ordinate? "))

    distance = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

    print(distance)

def travel_statistics():
    FULL_EFFICIENCY_KM_PER_LITRE = 5

    average_speed = float(input("What was the average speed? (kmh) "))
    duration = float(input("How long did you travel for? "))

    overall_distance = average_speed * duration
    print(overall_distance)

    amount_of_fuel_used = overall_distance / FULL_EFFICIENCY_KM_PER_LITRE
    print(amount_of_fuel_used)

def sum_of_squares():
    amount_of_squares = int(input("How many squars would you like to go up to? "))

    current_sum = 0
    for i in range(amount_of_squares):
        current_sum += i**2

    print(current_sum)

def average_of_numbers():
    amount_of_nums = int(input("How many numbers would you like have? "))

    current_sum = 0
    for i in range(amount_of_nums):
        num = int(input(f"What is your {i+1} number?"))
        current_sum += num
    
    average_num = current_sum / amount_of_nums
    print(average_num)

def fibonacci():
    seq = int(input("What postion of the fibonacci would you like? "))

    a, b = 0, 1
    for _ in range(seq):
        a, b = b, a + b
    print(a)

def select_coins():
    pence_amount = float(input("How many pence do you have? "))

    two_pounds_amount = pence_amount // 200
    pence_amount %= 200
    one_pound_amount = pence_amount // 100
    pence_amount %= 100
    fifty_pence_amount = pence_amount // 50
    pence_amount %= 50
    twenty_pence_amount = pence_amount // 20
    pence_amount %= 20
    ten_pence_amount = pence_amount // 10
    pence_amount %= 10
    five_pence_amount = pence_amount // 5
    pence_amount %= 5
    two_pence_amount = pence_amount // 2
    pence_amount %= 2
    one_pence_amount = pence_amount // 1
    pence_amount %= 1
    

    print(f"""You have
£2 Coins: {two_pounds_amount}
£1 Coins: {one_pound_amount}
Fifty Pence Coins: {fifty_pence_amount}
Twenty Pence Coins: {twenty_pence_amount}
Ten Pence Coins: {ten_pence_amount}
Five Pence Coins: {five_pence_amount}
Two Pence Coins: {two_pence_amount}
One Pence Coins: {one_pence_amount}
    """)

select_coins()