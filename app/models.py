class Source:
    
    def __init__(self,id,name,description,url,author):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.author = author

class Article:
    def __init__(self, title,image,url, description, postDate):
        self.title = title
        self.image = image
        self.url = url
        self.description = description
        self.postDate = postDate  