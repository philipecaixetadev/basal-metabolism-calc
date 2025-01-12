def request_info(mensagem):
    """Prompts the user for information and ensures that the input is a valid number."""
    while True:
        try:
            info = float(input(mensagem))
            return info 
        except ValueError:
            print("Error: Please enter a valid number.")

def request_optional_info(mensagem):
    """Prompts the user for optional information, allowing them to skip by pressing Enter."""
    while True:
        try:
            user_input = input(mensagem)
            if user_input.strip() == "":
                return None
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number or press Enter to skip.")

def request_gender():
    """Prompts the user to select a gender and ensures a valid input."""
    while True:
        gender = input("Enter your gender (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            return gender
        print("Error: Please enter 'male' or 'female'.")

if __name__ == "__main__":
    # Collecting user input for weight, height, age, and gender
    weight = request_info("Enter your weight in kilograms (kg): ")
    height = request_info("Enter your height in centimeters (cm): ")
    age = request_info("Enter your age in years: ")
    gender = request_gender()

    # Optional input for body fat percentage
    body_fat = request_optional_info("Enter your body fat percentage (or press Enter to skip): ")

    # Calculating the contributions to the BMR based on weight, height, and age
    if gender == "male":
        weight_result = weight * 13.4
        height_result = height * 4.8
        age_result = age * 5.7
        base_bmr = 88.36
    else:  # female
        weight_result = weight * 9.6
        height_result = height * 1.8
        age_result = age * 4.7
        base_bmr = 447.6

    # Base BMR calculation
    bmr = weight_result + height_result - age_result + base_bmr

    # Adjust BMR if body fat percentage is provided
    if body_fat is not None:
        lean_mass = weight * (1 - body_fat / 100)
        bmr = (370 + (21.6 * lean_mass))

    print(f"Your basal metabolic rate is {bmr:.2f} calories.")
