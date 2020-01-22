from flask import Blueprint, render_template, request, redirect, url_for 
import requests
import json
import pickle
import os

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
    lat = float(request.form.get('Latitude'))
    lon = float(request.form.get('Longitude'))
    print(lat)
    print(lon)

    polygon_id = get_polygon_id(lat, lon)
    print(polygon_id)

    return redirect(url_for('main.choose_option', polygon_id=polygon_id))

@main.route('/choose_option')
def choose_option():
    polygon_id = request.args['polygon_id']
    print("choose: ",polygon_id)
    return render_template('choose_option.html',  polygon_id=polygon_id)

@main.route('/statistics')
def statistics():
    filename = os.getcwd() + "/PlotPref/dict.txt"
    print(filename)
    f = open(filename, "rb")
    stat = pickle.load(f)
    print(stat)
    # {'number_of_harvests': 1, 'maturity_month': ['July'], 'harvested_month': ['August'], 'crop_cycle': 12.0, 'crop_type': 'crop X'}
    num_harvests = stat['number_of_harvests']
    maturity = stat['maturity_month'][0]
    harvest = stat['harvested_month'][0]
    crop_cycle = stat['crop_cycle']
    crop_type = stat['crop_type']
    return render_template('statistics.html', num_harvests = num_harvests, maturity = maturity, harvest = harvest, crop_cycle = crop_cycle, crop_type = crop_type)

@main.route('/cultivability')
def cultivability():
    polygon_id = "5e27c5ba4fcefd5559f914c6" #request.args.get('polygon_id')
    print("cult: ",request.args)
    r = "http://api.agromonitoring.com/agro/1.0/image/search?start=1559347200&end=1567296000&polyid=" + polygon_id + "&appid=026318a8ab9a39ab781720f8518353b1"
    print(r)
    stats = get_ndvi_data(r)
    stats_data = requests.get(stats).json()
    std = round(stats_data['std'], 2)
    min = round(stats_data['min'], 2)
    max = round(stats_data['max'], 2)
    mean = round(stats_data['mean'], 2)
    median = round(stats_data['median'], 2)
    cult = False
    if mean > 0.5:
        cult = True
    return render_template('cultivability.html', std = std, min = min, max = max, mean = mean, median = median, cult = cult)

@main.route('/current_status')
def current_status():
    return render_template('current_status.html')


def get_polygon_id(lat, lon):
    res = requests.post('http://api.agromonitoring.com/agro/1.0/polygons?appid=026318a8ab9a39ab781720f8518353b1', json={
    "name":"Polygon Sample",
    "geo_json":{
        "type":"Feature",
        "properties":{

        },
        "geometry":{
            "type":"Polygon",
            "coordinates":[
                [
                [lat+0.01,lon-0.01],
                [lat-0.01,lon-0.01],
                [lat-0.01,lon+0.01],
                [lat+0.01,lon+0.01],
                [lat+0.01,lon-0.01]
                ]
            ]
        }
    }
    })

    print(res.json())
    
    return res.json()['id']

def get_ndvi_data(r):
    res = requests.get(r)
    return res.json()[4]['stats']['ndvi']