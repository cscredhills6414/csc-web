from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)


# Configure MongoDB connection
client = MongoClient("mongodb+srv://cscredhilloffical:ABpa6ZuhuRYkJjau@cluster0.oyhzhdr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["registration_db"]
collection = db["registrations"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutcsc')
def aboutcsc():
    return render_template('pages/aboutcsc.html')

@app.route('/courses')
def courses():
    return render_template('pages/courses.html')
    
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

@app.route('/from')
def index():
    return render_template('registrations.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    mobile = request.form['mobile']
    whatsapp = request.form['whatsapp']
    status = request.form['status']

    # Insert data into MongoDB
    collection.insert_one({
        'name': name,
        'mobile': mobile,
        'whatsapp': whatsapp,
        'status': status
    })

    return redirect('/')

#courses

@app.route('/dca-p')
def dca_p():
    return render_template('pages/dca-p.html')

@app.route('/dca-t')
def dca_t():
    return render_template('pages/dca-t.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
