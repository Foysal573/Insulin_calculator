
# 💉 Insulin Dose Calculator

This is a simple Python project to calculate the recommended insulin dose based on carbohydrate intake, current blood glucose level, and insulin sensitivity (correction factor).

## 🧮 Features

- Calculates **meal insulin** based on carbs and ICR.
- Calculates **correction insulin** based on glucose deviation.
- Returns the **total insulin dose** needed.
- Simple command-line interface (CLI).
- Error handling for invalid input.

## 🧠 Formula Used
Total Insulin Dose = (Carbs ÷ ICR) + ((Current Glucose - Target Glucose) ÷ Correction Factor)
## 🚀 How to Run

1. Make sure you have Python installed (version 3+).
2. Clone this repository or download the `insulin_calculator.py` file.
3. Run the script using:

```bash
python insulin_calculator.py

Enter total carbohydrates (grams): 60
Enter Insulin-to-Carb Ratio (ICR): 10
Enter current blood glucose (mg/dL): 180
Enter target blood glucose (mg/dL): 120
Enter Correction Factor (CF): 50

🔹 Recommended insulin dose: 7.2 units




