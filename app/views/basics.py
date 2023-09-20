"""
WELCOME
"""
from flask import render_template, redirect, flash, url_for, abort, request, send_from_directory, current_app
from flask_mail import Message
from slugify import slugify

# our objects
from . import views


######################
#### STATIC PAGES ####
######################
# Displays the home page.
@views.route('/')
@views.route('/index')
@views.route('/index.html')
# Users must be authenticated to view the home page, but they don't have to have any particular role.
# Flask-Security will display a login form if the user isn't already authenticated.
def index():
    return render_template('pages/index.html')


@views.route('/about.html')
def about():
    return render_template('pages/about.html')

@views.route('/baby.html')
def baby():
    return render_template('pages/baby.html')

@views.route('/birthday.html')
def birthday():
    return render_template('pages/birthday.html')

@views.route('/bisque.html')
def bisque():
    return render_template('pages/bisque.html')

@views.route('/bridal.html')
def bridal():
    return render_template('pages/bridal.html')  

@views.route('/clay.html')
def clay():
    return render_template('pages/clay.html')

@views.route('/clayc.html')
def clayc():
    return render_template('pages/clayc.html')  

@views.route('/corporate.html')
def corporate():
    return render_template('pages/corporate.html')

@views.route('/fairy.html')
def fairy():
    return render_template('pages/fairy.html')

@views.route('/glass.html')
def glass():
    return render_template('pages/glass.html')

@views.route('/hours.html')
def hours():
    return render_template('pages/hours.html')

@views.route('/mobile.html')
def mobile():
    return render_template('pages/mobile.html')

@views.route('/party.html')
def party():
    return render_template('pages/party.html')

@views.route('/peace.html')
def peace():
    return render_template('pages/peace.html')

@views.route('/project.html')
def project():
    return render_template('pages/project.html')

@views.route('/rent.html')
def rent():
    return render_template('pages/rent.html')
@views.route('/summer.html')
def summer():
    return render_template('pages/summer.html')