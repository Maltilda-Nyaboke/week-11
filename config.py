import os
class Config:
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q{}-news&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
DEBUG = True