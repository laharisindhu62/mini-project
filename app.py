from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from diet_logic import generate_weekly_plan

app = Flask(__name__)
CORS(app)

QUESTIONS = [
    "What is your age?",
    "What is your weight (in kg)?",
    "What is your height (in cm)?",
    "What is your gender? (Male/Female/Other)",
    "What is your activity level? (low / moderate / high)",
    "What is your goal? (Weight loss / Weight gain / Maintain)",
    "Are you vegetarian or non-vegetarian?",
    "How many meals do you eat per day?",
    "Do you skip breakfast? (Yes/No)",
    "How much water do you drink daily (in liters)?",
    "How many hours do you sleep daily?",
    "Do you exercise regularly? (Yes/No)",
    "How many days per week do you exercise?",
    "What type of exercise do you do?",
    "Do you have diabetes? (Yes/No)",
    "Do you have hypertension? (Yes/No)",
    "Do you have obesity? (Yes/No)",
    "Do you have thyroid problems? (Yes/No)",
    "Do you have cholesterol issues? (Yes/No)",
    "Do you take any medicines regularly?",
    "Do you have food allergies?",
    "Are you lactose intolerant? (Yes/No)",
    "Do you consume junk food often? (Yes/No)",
    "Do you consume soft drinks? (Yes/No)",
    "Do you consume sugar daily? (Low/Medium/High)",
    "Do you drink alcohol? (Yes/No)",
    "Do you smoke? (Yes/No)",
    "How stressed are you daily? (Low/Medium/High)",
    "Do you eat late at night? (Yes/No)",
    "Do you feel hungry frequently? (Yes/No)",
    "Do you prefer home food or outside food?",
    "Do you eat fruits daily? (Yes/No)",
    "Do you eat vegetables daily? (Yes/No)",
    "Do you want vegetarian meal suggestions?",
    "Do you want non-vegetarian meal suggestions?",
    "Do you want calorie count included?",
    "Do you want a weekly diet plan?",
    "Do you want workout suggestions?",
    "Do you want yoga suggestions?",
    "Do you want diabetic-friendly meals?",
    "Do you want weight-loss recipes?",
    "Do you want weight-gain recipes?",
    "Do you want healthy snack ideas?",
    "Do you want water reminders?",
    "Do you want meal reminders?",
    "Do you want simple or detailed plans?",
    "Any food you strongly dislike?",
    "Any cultural food preference?",
    "Are you ready to get your personalized diet plan?"
]

user_session = {
    "step": 0,
    "answers": {}
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message")
    step = user_session["step"]

    if step > 0:
        user_session["answers"][QUESTIONS[step - 1]] = msg

    if step < len(QUESTIONS):
        reply = f"({step+1}/50) {QUESTIONS[step]}"
        user_session["step"] += 1
        return jsonify({"reply": reply})

    # Generate plan
    a = user_session["answers"]

    conditions = []
    if a.get("Do you have diabetes? (Yes/No)", "").lower() == "yes":
        conditions.append("diabetes")
    if a.get("Do you have hypertension? (Yes/No)", "").lower() == "yes":
        conditions.append("hypertension")
    if a.get("Do you have obesity? (Yes/No)", "").lower() == "yes":
        conditions.append("obesity")

    plan = generate_weekly_plan(
        age=a.get("What is your age?"),
        weight=a.get("What is your weight (in kg)?"),
        height=a.get("What is your height (in cm)?"),
        activity=a.get("What is your activity level? (low / moderate / high)"),
        conditions=conditions
    )

    user_session["step"] = 0
    user_session["answers"] = {}

    return jsonify({"reply": plan})

if __name__ == "__main__":
    app.run(debug=True)
