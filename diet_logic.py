def calculate_bmi(weight, height_cm):
    h = float(height_cm) / 100
    return round(float(weight) / (h * h), 2)

def get_base_calories(activity):
    if activity == "low":
        return 1800
    if activity == "moderate":
        return 2000
    return 2200

def adjust_calories(cal, conditions):
    if "diabetes" in conditions:
        cal -= 200
    if "hypertension" in conditions:
        cal -= 150
    if "obesity" in conditions:
        cal -= 250
    return max(cal, 1200)

def generate_weekly_plan(age, weight, height, activity, conditions):
    bmi = calculate_bmi(weight, height)
    base = get_base_calories(activity.lower())
    calories = adjust_calories(base, conditions)

    plan = f"""
📊 HEALTH SUMMARY
Age: {age}
BMI: {bmi}
Calories/day: {calories}

🍽 WEEKLY DIET PLAN
Breakfast: Oats + Fruit
Lunch: Chapati + Vegetables
Snack: Nuts + Green Tea
Dinner: Soup + Salad

✅ Stay hydrated & active!
"""
    return plan
