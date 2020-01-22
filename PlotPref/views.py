from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')
    
@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def sign_post():
    username = request.form.get('name')
    password = request.form.get('password')

    return redirect(url_for('main.location'))

@main.route('/location')
def location():
    return render_template('pick_location.html')

@main.route('/location', methods=['POST'])
def location_post():
    lat = request.form.get('Latitude')
    lon = request.form.get('Longitude')
    print(lat)
    print(lon)

    return redirect(url_for('main.choose_option'))

@main.route('/choose_option')
def choose_option():
    return render_template('choose_option.html')

@main.route('/statistics')
def statistics():
    return render_template('statistics.html')

@main.route('/cultivability')
def cultivability():
    return render_template('cultivability.html')

@main.route('/current_status')
def current_status():
    return render_template('current_status.html')