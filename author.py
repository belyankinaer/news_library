class Author:
    def __init__(self, name: str, login: str, password: str):
        self.name = name
        self._login = login
        self._password = password
        self._articles = []

    def get_name(self):
        return self.name

    def _check_credentials(self, login: str, password: str) -> bool:
        return self._login == login and self._password == password

    def write_article(self, name_article: str, text_article: str):
        from article import Article
        article = Article(name_article, text_article, self)
        self._articles.append(article)
        return article

    def get_articles(self):
        return self._articles
