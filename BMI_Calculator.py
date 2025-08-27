def take_input():
    while True:
        try:
            weight_input = input("Enter your weight (in kg): ").strip()
            height_input = input("Enter your height (in m): ").strip()

            if not weight_input or not height_input:
                raise ValueError("Inputs cannot be blank.")

            weight = float(weight_input)
            height = float(height_input)

            if not (5 <= weight <= 200):
                raise ValueError("Weight must be between 5 kg and 200 kg.")
            if not (0.2 <= height <= 2.5):
                raise ValueError("Height must be between 0.2 m and 2.5 m.")

            return weight, height

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please enter valid numeric values for weight and height.")

if __name__ == '__main__':
    w, h = take_input()
    bmi = w / (h ** 2)

    print(f"\nYour Body Mass Index is: {bmi}")
    print("Your BMI Category is:")

    if bmi < 18.5:
        print("You are Underweight!")
    elif 18.5 <= bmi < 25:
        print("You are Healthy (Normal Weight)!")
    elif 25 <= bmi < 30:
        print("You are Overweight!")
    else:
        print("You are Obese!")
        if 30 <= bmi < 35:
            print("You are in Obesity Class I!")
        elif 35 <= bmi < 40:
            print("You are in Obesity Class II!")
        else:
            print("You are in Obesity Class III (Severely Obese)!")