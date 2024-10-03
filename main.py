def request_info(mensagem):
    """Prompts the user for information and ensures that the input is a valid number."""
    # If the input is not valid, it displays an error message and prompts again.
    while True:
        try:
            info = float(input(mensagem))
            return info 
        except ValueError:
            print("Error: Please enter a valid number.")


if __name__ == "__main__":
    # Collecting user input for weight, height, and age using the request_info function
    weight = request_info("Enter your weigth in kilograms (kg): ")
    height = request_info("Enter your height in centimeters (cm): ")
    age = request_info("Enter your age in years: ")

    # Calculating the contributions to the BMR based on weight, height, and age
    weight_result = weight * 13.4
    height_result = height * 4.8
    age_result = age * 5.7

    # Calculating the Basal Metabolic Rate (BMR) using the contributions from weight, height, and age
    bmr = weight_result + height_result - age_result + 88.36 
    
    print(f"Your basal metabolism rate is {bmr:.2f} calories.")
