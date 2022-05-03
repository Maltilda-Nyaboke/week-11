from flask import render_template
from app import app
from .requests import get_sources,get_articles

# Views
@app.route('/')
def index():

    '''
      View root page function that returns the index page and its data
    '''
    title = "page name"
    sources = get_sources()
    return render_template('index.html', title=title, source=sources)

   
@app.route('/articles/<id>')
def articles(id):
    title = 'Articles page'
    articles = get_articles(id)
    return render_template('articles.html',title = title,article= articles)