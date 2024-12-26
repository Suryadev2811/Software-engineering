# 1)Hardcoded coefficients
a = 1
b = -3
c = 2

# Simulating weather modeling using a quadratic formula
def quadratic_solution(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None
    else:
        return None, None

print("Hardcoded roots:", quadratic_solution(a, b, c))

# 2)user given input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

def calculate_weather_prediction(temperature, humidity, wind_speed):
    """Calculates the weather prediction (W) using the quadratic model."""
    W = 0.5 * (temperature**2) - 0.2 * humidity + 0.1 * wind_speed - 15
    return W

def map_prediction_to_category(W):
    """Maps the calculated W value to a weather category."""
    if W > 25:
        return "Sunny"
    elif 15 < W <= 25:
        return "Cloudy"
    elif 5 < W <= 15:
        return "Rainy"
    else:
        return "Stormy"

2.def get_weather_prediction(temperature, humidity, wind_speed):
    """Gets the weather prediction and category."""
    W = calculate_weather_prediction(temperature, humidity, wind_speed)
    category = map_prediction_to_category(W)
    return category, W  # Return both the category and W value


def main():
    """Main function to handle user input and output."""
    mode = input("Enter input mode ('manual' or 'file'): ").lower()

    if mode == "manual":
        temperature = float(input("Enter temperature: "))
        humidity = float(input("Enter humidity: "))
        wind_speed = float(input("Enter wind speed: "))
        category, W = get_weather_prediction(temperature, humidity, wind_speed)
        print(f"Weather prediction: {category} (W = {W:.2f})")

    elif mode == "file":
        try:
            with open("spam.txt", "r") as file:
                for line_num, line in enumerate(file, 1):
                    try:
                        data = [float(value) for value in line.strip().split()]
                        if len(data) == 3:  # Make sure there are 3 values per line
                            temperature, humidity, wind_speed = data
                            category, W = get_weather_prediction(temperature, humidity, wind_speed)
                            print(f"Weather prediction for line {line_num}: {category} (W = {W:.2f})")
                        else:
                            print(f"Warning: Invalid data on line {line_num}. Skipping.")
                    except ValueError:
                        print(f"Warning: Invalid data on line {line_num}. Skipping.")

        except FileNotFoundError:
            print("Error: spam.txt not found.")

    else:
        print("Invalid input mode. Please enter 'manual' or 'file'.")

if __name__ == "__main__":
    main()

roots = quadratic_solution(a, b, c)
print("Roots from user input:", roots)
