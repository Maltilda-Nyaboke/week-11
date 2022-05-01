import os

class Config:
    '''
    General configuration parent class
    '''
    
NEWS_API_KEY = 'a10c481237fa4068b0ef87679cdd1490'
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?q{}-news&apiKey={}'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
