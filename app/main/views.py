from flask import render_template,request,redirect,url_for
from app.main import app
from . import main
from ..requests import get_article,get_source,search_source
from ..models import Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')