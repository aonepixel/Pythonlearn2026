from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    display_value = ""
    if request.method == "POST":
        # Get data from the form buttons
        current_display = request.form.get("display", "")
        action = request.form.get("action")

        if action == "C":
            display_value = ""
        elif action == "=":
            try:
                # Safely evaluate the mathematical string expression
                # Replacing visual operators with Python native operators
                sanitized_expr = current_display.replace("×", "*").replace("÷", "/")
                display_value = str(eval(sanitized_expr))
            except Exception:
                display_value = "Error"
        else:
            # Append the button value to the existing display expression
            display_value = current_display + action
    return render_template("calculator.html", display=display_value)

if __name__ == "__main__":
    app.run(debug=True)
