from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    FName = 'Muhammad '
    LName = 'Tahir Aslam'
    return render_template('index.html', FName = FName, LName = LName)

app.run(debug=True)