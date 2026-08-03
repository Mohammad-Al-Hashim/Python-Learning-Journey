print("""
Welcome to the BMI Calculator!
This program calculates your Body Mass Index (BMI) based on your weight and height,
and tells you which category you fall into: Underweight, Normal, Overweight, or Obese.
""")
weight = float(input("Please type your weight in kilogram: "))
height = float(input("Please type your height in centimeters: "))
bmi = weight / ((height/100)**2)
if bmi < 18.5:
    print(f"Your BMI is: {bmi}. You are classified as: underweight (less than 18.5)")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is: {bmi}. You are classified as: normal (between 18.5 and 25)")
elif bmi >= 25 and bmi < 29.9:
    print(f"Your BMI is: {bmi}. You are classified as: overweight (between 25 and 29.9)")
else:
    print(f"Your BMI is: {bmi}. You are classified as: obese (30 and above)")
