class Author:
    def __init__(self, name: str, login: str):
        self._name = name
        self._login = login
        self._articles = []

    def get_name(self):
        return self._name

    def get_login(self):
        return self._login

    def get_articles(self):
        return self._articles

    def write_article(self, name_article: str, text_article: str):
        from article import Article
        article = Article(name_article, text_article, self)
        self._articles.append(article)
        return article
