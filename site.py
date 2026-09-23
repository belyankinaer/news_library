from author import Author


class Site:
    def __init__(self, name: str):
        self._name = name
        self._articles = {}
        self._users = []

    def get_name(self):
        return self._name

    def register_author(self, author: Author):
        if author not in self._users:
            self._users.append(author)
            print(f'Автор {author.name} зарегистрирован на сайте')

    def login_author(self, login: str, password: str) -> Author | None:
        for author in self._users:
            if author._check_credentials(login, password):
                print(f'Автор {author.name} успешно вошёл на сайт')
                return author
        print('Неверный логин или пароль')
        return None

    def add_article(self, article):
        if article.get_site() is not None:
            print(f'Статья "{article.get_name()}" уже опубликована на сайте')
            return
        name_article = article.get_name()
        self._articles[name_article] = article
        article.upload_to_site(self)

    def run(self):
        print(f'Сайт "{self._name}" запущен')

    def down(self):
        print(f'Сайт "{self._name}" выключен')

    def show_articles(self):
        print(f'\nСтатьи на сайте "{self._name}":')
        for title in self._articles:
            article = self._articles[title]
            author_name = article.get_author().get_name()
            print(f'  • "{title}" — автор: {author_name}')
        print()
