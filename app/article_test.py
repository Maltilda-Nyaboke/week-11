import unittest
from models import articles
Article = articles.Article

class ArticleTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Article("Ferns aren’t nearly as fickle as you fear","https://i.guim.co.uk/img/media/19bd332853c3bc31f2ece9d2f7550266a631afca/0_412_5466_3280/master/5466.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdG8tZGVmYXVsdC5wbmc&enable=upscale&s=cf8cba3e23a95653583ffd81224c5c14","They’re reputed to be immensely difficult to grow. That’s nonsenseThere are some pieces of received wisdom in horticulture that are so frequently repeated, it can seem as if they simply must be true. Like the idea cacti are hard to kill, despite the fact this…","http","2022-05-01T07:15:17Z")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

if __name__ == '__main__':
    unittest.main()