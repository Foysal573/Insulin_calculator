
def calculate_insulin(carbs, icr, current_glucose, target_glucose, correction_factor):
    meal_insulin = carbs / icr
    correction_insulin = (current_glucose - target_glucose) / correction_factor
    total_insulin = meal_insulin + correction_insulin

    return round(total_insulin, 2)


def main():
    print("=== Insulin Dose Calculator ===")

    try:
        carbs = float(input("Enter total carbohydrates (grams): "))
        icr = float(input("Enter Insulin-to-Carb Ratio (ICR): "))
        current_glucose = float(input("Enter current blood glucose (mg/dL): "))
        target_glucose = float(input("Enter target blood glucose (mg/dL): "))
        correction_factor = float(input("Enter Correction Factor (CF): "))

        dose = calculate_insulin(carbs, icr, current_glucose, target_glucose, correction_factor)
        print(f"\n🔹 Recommended insulin dose: {dose} units")
    except ValueError:
        print("❌ Please enter valid numeric values.")


if __name__ == "__main__":
    main()
