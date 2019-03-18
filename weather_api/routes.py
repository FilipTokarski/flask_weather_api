from flask import render_template, request, redirect, url_for
from weather_api import app, db
from .models import Cities
from .api_request import ApiRequest
from time import sleep


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            city_name = request.form['city']
            api_request = ApiRequest(city_name)
            api_data = api_request.get_data()
            if type(api_data) == dict:
                db.session.add(Cities(city=api_data['name'], 
                                    temp=api_data['temp'],
                                    icon=api_data['icon'],
                                    weather=api_data['weather']))
                db.session.commit()
                cities = Cities.query.all()
                cities.reverse() #should reverse in query above?
                return render_template('home.html', context=cities)
            elif type(api_data) == str:
                return render_template('home.html', message=api_data)
        except:
            return render_template('home.html',
                                    message="Sorry, something went wrong.")

    elif request.method == 'GET':
        cities = Cities.query.all()
        cities.reverse()
        return render_template('home.html', context=cities)


@app.route('/delete_city/<id>')
def delete_city(id):
    try:
        city = Cities.query.filter_by(id=id).first()
        db.session.delete(city)
        db.session.commit()
        sleep(0.4) 
        return redirect('/')
    except:
        return render_template('home.html', 
                                message="Sorry, something went wrong.")
