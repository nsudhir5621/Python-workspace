from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log')
def log_visit():
    try:
        with open('visits.txt', 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"visit at {timestamp}\n")
        return "Visit logged successfully"
    except Exception as e:
        return f"error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
