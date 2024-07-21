from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutcsc')
def aboutcsc():
    return render_template('pages/aboutcsc.html')

@app.route("/locations")
def locations():
    return render_template('locations/locations.html')

@app.route("/django")
def django():
    return render_template('pages/django.html')

@app.route("/microsoft")
def microsoft():
    return render_template('pages/microsoft.html')

@app.route("/python")
def python():
    return render_template('pages/python.html')

@app.route("/react")
def react():
    return render_template('pages/react.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
