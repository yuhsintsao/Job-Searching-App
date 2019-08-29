from flask import Blueprint, render_template, request, session, current_app
from models.menu import Menu
from models.auth import required_login

menu_blueprint = Blueprint('menu', __name__)

@menu_blueprint.route('/getstart', methods=['GET','POST'])
@required_login
def getstart():
    if request.method == "GET":
        return render_template('menu/menu.html')
    else:
        search_for = request.form['selected']
        session['search'] = search_for       
        return render_template('menu/menu.html', search=search_for)

@menu_blueprint.route('/openings', methods=['GET', 'POST'])
@required_login
def menu():
    form = request.form
    if session['search'] == "Job Openings":
        result = Menu().search_job(form['start'], form['end'], form['title']).sort_values(by=['update_date'], ascending=False)
        return render_template('menu/jobs.html', results=result)   
    elif session['search'] == "Company":
        result = Menu().search_company(form['location'], form['region'], form['country'])
        return render_template('menu/company.html', results=result)
    elif session['search'] == "Both":
        df = Menu().search_both(form['start'], form['end'], form['title'], form['location'], form['region'], form['country'])
        result = Menu().group_by(df, 'locality').sort_values(by='count', ascending=False)
        return render_template('menu/openings.html', results=result)

@menu_blueprint.route('/map', methods=['GET', 'POST'])
@required_login
def map():
    if request.method == "POST":
        if 'company' in request.form:
            company = request.form['company']
            continent = request.form['continent']
            current_app.logger.info(continent)
            return render_template('menu/map.html', continent=continent)
        if 'title' in request.form:
            form = request.form
            result = Menu().search_job(form['start'], form['end'], form['title']).sort_values(by=['update_date'], ascending=False)
            current_app.logger.info("Get the titles")
            return render_template('menu/map.html', results=result)   
    return render_template('menu/map.html')