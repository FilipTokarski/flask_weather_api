from flask import render_template, request, redirect, url_for
from weather_api import app, db
from weather_api.models import Cities
from weather_api.api_request import ApiRequest
from sqlalchemy import desc


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['city']
        api_data = ApiRequest(city_name)
        context = api_data.get_data()
       
        db.session.add(Cities(city=context['name'], 
                            temp=context['temp'],
                            icon=context['icon'],
                            weather=context['weather']))
        db.session.commit()
        cities = Cities.query.all()
        cities.reverse()
        return render_template('home.html', context=cities)

    elif request.method == 'GET':
        cities = Cities.query.all()
        return render_template('home.html', context=cities)


@app.route('/delete_city', methods=['GET', 'POST'])
def delete_city():
    if request.method == 'POST':
        modal = request.form['modal']
        return redirect('/')

    elif request.method == 'GET':
        return redirect('/')
