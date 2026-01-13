from flask import Flask, render_template, request

app = Flask(__name__)

# Same common passwords list as your original code
COMMON_PASSWORDS = [
    'password', '123456', 'qwerty', 'abc123', '12345678',
    'password1', '111111', 'welcome', 'admin', 'letmein'
]

def check_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 25
        feedback.append("✓ Good length (8+ characters)")
    else:
        feedback.append("✗ Too short - need at least 8 characters")

    # Uppercase
    if any(char.isupper() for char in password):
        score += 25
        feedback.append("✓ Contains uppercase letter")
    else:
        feedback.append("✗ Add at least one uppercase letter (A-Z)")

    # Lowercase
    if any(char.islower() for char in password):
        score += 25
        feedback.append("✓ Contains lowercase letter")
    else:
        feedback.append("✗ Add at least one lowercase letter (a-z)")

    # Number
    if any(char.isdigit() for char in password):
        score += 25
        feedback.append("✓ Contains number")
    else:
        feedback.append("✗ Add at least one number (0-9)")

    # Special char (bonus)
    if any(not char.isalnum() for char in password):
        score += 10
        feedback.append("✓ Contains special character (bonus!)")

    # Common password check (kills score)
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.insert(0, "⚠ WARNING: This is a commonly used password!")

    return score, feedback

def get_strength_label(score):
    if score < 25:
        return "Very Weak"
    elif score < 50:
        return "Weak"
    elif score < 75:
        return "Medium"
    elif score < 100:
        return "Strong"
    else:
        return "Very Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form.get("password", "").strip()

        if password:
            score, feedback = check_password(password)
            label = get_strength_label(score)
            # Never send real password back — only stars
            masked = "*" * len(password)

            result = {
                "masked": masked,
                "score": score,
                "label": label,
                "feedback": feedback
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)