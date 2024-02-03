from flask import Flask, render_template, request
from flask_applicationinsights import AppInsights

app = Flask(__name__)
app.config['APPLICATIONINSIGHTS_INSTRUMENTATIONKEY'] = 'b17d2ea3-f1c6-4e58-a114-9b0b8f15a265'
appinsights = AppInsights(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Dane przesłane! Imię: {name}, Email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
