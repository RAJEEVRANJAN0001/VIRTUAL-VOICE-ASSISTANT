from datetime import datetime
import pickle
import math
from utilities import takeCommand, speak


def calculator_operation(num1, num2, operation):
    if operation == "addition":
        return num1 + num2
    elif operation == "subtraction":
        return num1 - num2
    elif operation == "multiplication":
        return num1 * num2
    elif operation == "division":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "modulus":
        return num1 % num2
    elif operation == "power":
        return num1 ** num2
    elif operation == "square root":
        return math.sqrt(num1)
    elif operation == "sine":
        return math.sin(math.radians(num1))
    elif operation == "cosine":
        return math.cos(math.radians(num1))
    elif operation == "tangent":
        return math.tan(math.radians(num1))
    elif operation == "exponential":
        return math.exp(num1)
    elif operation == "logarithm":
        return math.log(num1) if num1 > 0 else "Error: Logarithm of non-positive number"
    elif operation == "factorial":
        return math.factorial(int(num1))
    elif operation == "percentage":
        return (num1 / 100) * num2
    elif operation == "absolute value":
        return abs(num1)
    else:
        return "Unsupported operation"
def save_to_history(operation, result):
    try:
        with open('calculator_history.pkl', 'rb') as file:
            history = pickle.load(file)
    except FileNotFoundError:
        history = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({'time': current_time, 'operation': operation, 'result': result})
    with open('calculator_history.pkl', 'wb') as file:
        pickle.dump(history, file)
def perform_calculator_operation():
    speak("Please specify the operation: addition, subtraction, multiplication, division, modulus, power, square root, sine, cosine, tangent, exponential, logarithm, factorial, percentage, or absolute value.")
    operation = takeCommand().lower()

    if operation in ["power", "square root", "sine", "cosine", "tangent", "exponential", "logarithm", "factorial"]:
        speak(f"Sure! Please provide the number for {operation}.")
        num1 = float(takeCommand())
        result = calculator_operation(num1, None, operation)
        speak(f"The {operation} of {num1} is {result}.")
        save_to_history(f"{operation} of {num1}", result)
    elif operation == "percentage":
        speak("Please provide the base number.")
        num1 = float(takeCommand())
        speak("Now, please provide the percentage.")
        num2 = float(takeCommand())
        result = calculator_operation(num1, num2, operation)
        speak(f"{num2}% of {num1} is {result}.")
        save_to_history(f"{num2}% of {num1}", result)
    elif operation == "absolute value":
        speak("Please provide the number for which you want to find the absolute value.")
        num1 = float(takeCommand())
        result = calculator_operation(num1, None, operation)
        speak(f"The absolute value of {num1} is {result}.")
        save_to_history(f"Absolute value of {num1}", result)
    else:
        speak("Please specify the first number.")
        num1 = float(takeCommand())
        speak("Now, please specify the second number.")
        num2 = float(takeCommand())
        result = calculator_operation(num1, num2, operation)
        speak(f"The result is {result}.")
        save_to_history(f"{operation}", result)

def retrieve_history():
    try:
        with open('calculator_history.pkl', 'rb') as file:
            history = pickle.load(file)

        if not history:
            speak("Calculator history is empty.")
        else:
            speak("Calculator history:")
            for entry in history:
                speak(f"At {entry['time']}: {entry['operation']} = {entry['result']}")
    except FileNotFoundError:
        speak("Calculator history is empty.")
def perform_advanced_calculations():
    speak("This is an advanced calculation. Please provide the required inputs and operation.")
    operation = takeCommand().lower()

    if operation == "calculate volume of sphere":
        calculate_volume_of_sphere()
    elif operation == "calculate area of triangle":
        calculate_area_of_triangle()
    elif operation == "calculate area of circle":
        calculate_area_of_circle()
    elif operation == "calculate perimeter of rectangle":
        calculate_perimeter_of_rectangle()
    elif operation == "calculate area of square":
        calculate_area_of_square()
    else:
        speak("Unsupported advanced operation.")
def calculate_volume_of_sphere():
    speak("Sure! Please provide the radius of the sphere.")
    radius = float(takeCommand())
    volume = (4 / 3) * math.pi * (radius ** 3)
    speak(f"The volume of the sphere with radius {radius} is {volume}.")
    save_to_history(f"Volume of sphere with radius {radius}", volume)
def calculate_area_of_triangle():
    speak("Sure! Please provide the base and height of the triangle.")
    base = float(takeCommand())
    height = float(takeCommand())
    area = 0.5 * base * height
    speak(f"The area of the triangle with base {base} and height {height} is {area}.")
    save_to_history(f"Area of triangle with base {base} and height {height}", area)
def calculate_area_of_circle():
    speak("Sure! Please provide the radius of the circle.")
    radius = float(takeCommand())
    area = math.pi * (radius ** 2)
    speak(f"The area of the circle with radius {radius} is {area}.")
    save_to_history(f"Area of circle with radius {radius}", area)
def calculate_perimeter_of_rectangle():
    speak("Sure! Please provide the length and width of the rectangle.")
    length = float(takeCommand())
    width = float(takeCommand())
    perimeter = 2 * (length + width)
    speak(f"The perimeter of the rectangle with length {length} and width {width} is {perimeter}.")
    save_to_history(f"Perimeter of rectangle with length {length} and width {width}", perimeter)
def calculate_area_of_square():
    # Placeholder functions
    speak("Make sure to provide the length of one side of the square.")
    length = float(takeCommand())  # Placeholder function to get user input
    area = length * length
    speak(f"The area of the square with the length of one side {length} is {area}.")
    save_to_history(f"The area of the square is {area}.")