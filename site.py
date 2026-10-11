from article import Article
from author import Author


class Site:
    def __init__(self, name: str):
        self._name = name
        self._articles = {}
        self._users = []
        self._passwords = {}

    def get_name(self):
        return self._name

    def run(self):
        print(f'Сайт "{self._name}" запущен')

    def down(self):
        print(f'Сайт "{self._name}" выключен')

    def register_author(self, author: Author, password: str):
        author_name = author.get_name()

        if author not in self._users:
            self._users.append(author)
            self._passwords[author.get_login()] = password

            print(f'Автор {author_name} зарегистрирован на сайте')
        else:
            self._passwords[author.get_login()] = password

            print(f'Автор {author_name} обновлён на сайте')

    def check_credentials(self, login: str, password: str) -> bool:
        stored_password = self._passwords.get(login)
        return stored_password is not None and stored_password == password

    def login_author(self, login: str, password: str) -> Author | None:
        if not self.check_credentials(login, password):
            print('Неверный логин или пароль')
            return None
        
        for author in self._users:
            if author.get_login() == login:
                author_name = author.get_name()
                print(f'Автор {author_name} успешно вошёл на сайт')
                return author
            
        return None

    def add_article(self, article, author: Author):
        if not self.is_article_on_site(article):
            return
        if not self.is_author_registered(author):
            return

        name_article = article.get_name()
        self._articles[name_article] = article
        article.upload_to_site(self)

    def is_article_on_site(self, article: Article) -> bool:
        if article.get_site() is not None:
            print(f'Статья "{article.get_name()}" уже опубликована на сайте')
            return False
        return True

    def is_author_registered(self, author: Author) -> bool:
        if author not in self._users:
            print(f'Автор "{author.get_name()}" не зарегистрирован на сайте')
            return False
        return True
    

    def get_articles(self):
        print(f'\nСтатьи на сайте "{self._name}":')

        for title in self._articles:
            article = self._articles[title]
            author_name = article.get_author_name().get_name()
            print(f'  • "{title}" — автор: {author_name}')

