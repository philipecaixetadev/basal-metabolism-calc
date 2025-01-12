# Basal Metabolic Rate (BMR) Calculator

This project is a Python-based calculator for estimating Basal Metabolic Rate (BMR). It supports various features, including gender-specific calculations and optional body fat percentage adjustments. The tool is designed to be user-friendly and flexible, providing accurate results tailored to individual inputs.

---

## Features

- **Gender Selection**: Users can specify their gender (male/female) for more accurate BMR calculations.
- **Body Fat Percentage**: Allows users to input their body fat percentage (optional). If provided, the calculator adjusts the BMR based on lean body mass.
- **Dynamic Input Validation**: Ensures all numeric inputs are valid, reducing errors.
- **Backward Compatibility**: Works seamlessly even if optional inputs are skipped.

---

## How It Works

1. **Input Required Information**:
   - Weight (in kilograms).
   - Height (in centimeters).
   - Age (in years).
2. **Select Gender**:
   - Male or Female.
3. **Optional Input**:
   - Body fat percentage (press Enter to skip).
4. **Calculation Logic**:
   - For males:
     
BMR = (13.4 * weight) + (4.8 * height) - (5.7 * age) + 88.36

   - For females:
     
BMR = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 447.6

   - If body fat percentage is provided:
     
Lean Mass = weight * (1 - body_fat / 100)
     BMR = 370 + (21.6 * Lean Mass)


---

## Requirements

- Python 3.6+

---

## How to Run

1. Clone the repository:
   
bash
   git clone https://github.com/philipecaixetadev/basal-metabolism-calc

2. Navigate to the project directory:
   
bash
   cd location

3. Run the script:
   
bash
   python bmr_calculator.py


---

## Example Usage

### Input Example:
Enter your weight in kilograms (kg): 70
Enter your height in centimeters (cm): 175
Enter your age in years: 25
Enter your gender (male/female): male
Enter your body fat percentage (or press Enter to skip): 15


### Output Example:
Your basal metabolic rate is 1782.20 calories.


---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features:

1. Fork this repository.
2. Create a feature branch:
   
bash
   git checkout -b feature-name

3. Commit your changes:
   
bash
   git commit -m "Add feature-name"

4. Push to the branch:
   
bash
   git push origin feature-name

5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or suggestions, feel free to contact me via my [GitHub profile](https://github.com/philipecaixetadev).
