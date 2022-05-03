from app import app
import urllib.request,json
from .models import articles, sources

Article = articles.Article
Source = sources.Source

api_key = app.config['NEWS_API_KEY']
base_source_url = app.config['SOURCES_URL']
base_article_url = app.config['ARTICLES_URL']



def get_articles(id):
    get_articles_url = base_article_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url)as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        article_results = None

        if get_articles_response['articles']:

            article_results = get_articles_response['articles']
            article_results =  process_articles(article_results)

    return article_results
    

def process_articles(article_list):
    article_results = []
    for article in article_list:
        title = article.get('title')
        url = article.get('url')
        image = article.get('urlToImage')
        description = article.get('description')
        postDate = article.get('publishedAt')

        if postDate :
            article_object = Article(title, image,url, description, postDate)
            article_results.append(article_object)
            
    return article_results





def get_sources():
    get_sources_url = base_source_url.format(api_key)
    with urllib.request.urlopen(get_sources_url)as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None

        if get_sources_response ['sources']:
            source_results_list = get_sources_response['sources']
            source_results =  process_results(source_results_list)

    return source_results

def process_results(source_list):
    source_results = []
    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        author = source.get('author')

        if id :
            source_object = Source(id, name, description, url, author)
            source_results.append(source_object)
            
    return source_results





