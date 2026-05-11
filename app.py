from flask import Flask, render_template, request

app = Flask(__name__)

positive_habits = [
    "exercise",
    "study",
    "reading",
    "meditation",
    "healthy food",
    "sleep early",
    "drink water"
]

negative_habits = [
    "smoking",
    "junk food",
    "late sleep",
    "social media",
    "skip workout",
    "procrastination"
]

@app.route('/', methods=['GET', 'POST'])
def home():
    result = []
    positive_count = 0
    negative_count = 0
    score = 0
    suggestion = ""

    if request.method == 'POST':
        user_input = request.form['habits'].lower()
        habits = [habit.strip() for habit in user_input.split(',')]

        for habit in habits:
            if habit in positive_habits:
                result.append(f"✅ Good Habit: {habit}")
                positive_count += 1

            elif habit in negative_habits:
                result.append(f"❌ Bad Habit: {habit}")
                negative_count += 1

            else:
                result.append(f"⚪ Unknown Habit: {habit}")

        score = positive_count - negative_count

        if score >= 3:
            suggestion = "Excellent lifestyle!"
        elif score >= 1:
            suggestion = "Good progress."
        else:
            suggestion = "Need improvement."

    return render_template(
        'index.html',
        result=result,
        positive_count=positive_count,
        negative_count=negative_count,
        score=score,
        suggestion=suggestion
    )

if __name__ == '__main__':
    app.run(debug=True)
positive_habits = ["exercise", "study", "reading", "meditation", "healthy food", "sleep early", "drink water" ]

negative_habits = [ "smoking", "junk food", "late sleep", "social media", "skip workout",

"procrastination" ]

print("===== HABIT DETECTION SYSTEM =====")

user_input = input("Enter today's habits separated

by commas: ").lower()

habits = [habit.strip() for habit in user_input.split(",")]

positive_count = 0 negative_count = 0

print("\nDetected Habits:")

for habit in habits: if habit in positive_habits: print(f" Good Habit: {habit)") positive_count +=

1
elif habit in negative_habits:

print(f"X Bad Habit:

{habit}")

negative_count += 1

else:

print(f" Unknown Habit: {habit}")
