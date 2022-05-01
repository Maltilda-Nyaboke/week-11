class Article:
    def __init__(self,title,urlToImage,description,publishedAt):
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.publishedAt = publishedAt

class Source:
    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url        