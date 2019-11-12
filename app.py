from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    """Renders the home page with links to Fortune."""
    return render_template('index.html')

@app.route('/fortune')
def fortune_form():
    """Renders the fortune page."""
    return render_template('fortune.html')

@app.route('/fortune_result')
def fortune_result():
    users_name = request.args.get('name')
    users_month = request.args.get('month')
    drink = request.args.get('tell_fortune')

    if drink == "1" and ("E" or "e" in users_name):
        fortune = "You'll experience a magical day!"
    elif len(users_name) >= 0 and drink != "1" and users_month == "1":
        fortune= "Your day will suprise you!"
    elif users_month == "2" or users_month == "3" and drink != "1":
        fortune= "You will have a wonderful day!"
    else:
        fortune= "You will have a terrific day!"

    return render_template('fortune_result.html', fortune=fortune)
