def calculator_bmi():
    print("Welcome to the BMI Calculator!")
#1.Age Input and Validation
    while True:
        try:
            age = int(input("Please enter your age in years: "))
            if age <= 0:
                print("Age must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")
            
    # 2. Weight Input and Validation
    while True:
        try:
            weight = float(input("Please enter your weight in kilograms (kg): "))
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for weight.")

    # 3. Height Input and Validation
    while True:
        try:
            height = float(input("Please enter your height in meters (m): "))
            if height <= 0:
                print("Height must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for height.")

    # 3. BMI Calculation
    bmi = weight / (height ** 2)
    rounded_bmi = round(bmi, 2)

    # 4. Categorization of BMI
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    # 5. Displaying the Result
    print("\n--------------------------------------------")
    print(f"Your BMI is: {rounded_bmi}")
    print(f"Category: {category}")
    print("--------------------------------------------")

# To run the program
if __name__ == "__main__":
    calculator_bmi()